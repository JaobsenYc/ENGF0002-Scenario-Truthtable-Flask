"""
    admin apis
    ~~~~~~~~~
    :copyright: © 2020 by the Lin team.
    :Copyright (c) 2021 Chen Yang, Siqi Zhu,Jeffrey Li,Minyi Lei
    :license: MIT, see LICENSE for more details.
"""
import math

from flask import request
from lin import find_user, get_ep_infos, manager, permission_meta
from lin.db import db
from lin.enums import GroupLevelEnum
from lin.exception import Forbidden, NotFound, ParameterError, Success
from lin.jwt import admin_required
from lin.logger import Logger
from lin.redprint import Redprint
from sqlalchemy import func

from app.util.page import get_page_from_query, paginate
from app.validator.form import (
    DispatchAuth,
    DispatchAuths,
    NewGroup,
    RemoveAuths,
    ResetPasswordForm,
    UpdateGroup,
    UpdateUserInfoForm,
)

admin_api = Redprint("admin")


@admin_api.route("/permission")
@permission_meta(name="查询所有可分配的权限", module="管理员", mount=False)
@admin_required
def permissions():
    return get_ep_infos()


@admin_api.route("/users")
@permission_meta(name="查询所有用户", module="管理员", mount=False)
@admin_required
def get_admin_users():
    start, count = paginate()
    group_id = request.args.get("group_id")
    # filter root group
    query_root_group_id = db.session.query(manager.group_model.id).filter(
        manager.group_model.level == GroupLevelEnum.ROOT.value
    )
    _user_groups_list = db.session.query(
        manager.user_group_model.user_id.label("user_id"),
        func.group_concat(manager.user_group_model.group_id).label("group_ids"),
    ).filter(~manager.user_group_model.group_id.in_(query_root_group_id))
    if group_id:
        _user_groups_list = _user_groups_list.filter(
            manager.user_group_model.group_id == group_id
        )
    user_groups_list = (
        _user_groups_list.group_by(manager.user_group_model.user_id)
        .offset(start)
        .limit(count)
        .all()
    )

   # filter root group
    _total = db.session.query(
        func.count(func.distinct(manager.user_group_model.user_id))
    ).filter(~manager.user_group_model.group_id.in_(query_root_group_id))
    if group_id:
        _total = _total.filter(manager.user_group_model.group_id == group_id)
    total = _total.scalar()

    # get user info
    user_ids = [x.user_id for x in user_groups_list]
    users = manager.user_model.query.filter(manager.user_model.id.in_(user_ids)).all()
    user_dict = dict()
    for user in users:
        user.groups = list()
        user._fields.append("groups")
        user_dict[user.id] = user

    if not group_id:
        group_ids = [
            int(i)
            for i in set().union(*(x.group_ids.split(",") for x in user_groups_list))
        ]
        groups = manager.group_model.query.filter(
            manager.group_model.id.in_(group_ids)
        ).all()
        group_dict = dict()
        for group in groups:
            group_dict[group.id] = group
        items = []

        for user_id, group_ids in user_groups_list:
            group_id_list = [int(gid) for gid in group_ids.split(",")]
            groups = [group_dict[group_id] for group_id in group_id_list]
            user_dict[user_id].groups = groups
            items.append(user_dict[user_id])

    total_page = math.ceil(total / count)
    page = get_page_from_query()
    return {
        "count": count,
        "items": users,
        "page": page,
        "total": total,
        "total_page": total_page,
    }


@admin_api.route("/user/<int:uid>/password", methods=["PUT"])
@permission_meta(name="修改用户密码", module="管理员", mount=False)
@admin_required
def change_user_password(uid):
    form = ResetPasswordForm().validate_for_api()

    user = find_user(id=uid)
    if user is None:
        raise NotFound("用户不存在")

    with db.auto_commit():
        user.reset_password(form.new_password.data)

    return Success("密码修改成功")


@admin_api.route("/user/<int:uid>", methods=["DELETE"])
@permission_meta(name="删除用户", module="管理员", mount=False)
@Logger(template="管理员删除了一个用户")
@admin_required
def delete_user(uid):
    user = manager.user_model.get(id=uid)
    if user is None:
        raise NotFound("用户不存在")
    groups = manager.group_model.select_by_user_id(uid)
    # only one root group
    if groups[0].level == GroupLevelEnum.ROOT.value:
        raise Forbidden("无法删除此用户")
    with db.auto_commit():
        manager.user_group_model.query.filter_by(user_id=uid).delete(
            synchronize_session=False
        )
        user.hard_delete()
    return Success("操作成功")


@admin_api.route("/user/<int:uid>", methods=["PUT"])
@permission_meta(name="管理员更新用户信息", module="管理员", mount=False)
@admin_required
def update_user(uid):
    form = UpdateUserInfoForm().validate_for_api()

    user = manager.user_model.get(id=uid)
    if user is None:
        raise NotFound("用户不存在")
    if user.email != form.email.data:
        exists = manager.user_model.get(email=form.email.data)
        if exists:
            raise ParameterError("邮箱已被注册，请重新输入邮箱")
    with db.auto_commit():
        user.email = form.email.data
        group_ids = form.group_ids.data
        # clear joint data
        manager.user_group_model.query.filter_by(user_id=user.id).delete(
            synchronize_session=False
        )
        user_group_list = list()
        if len(group_ids) == 0:
            group_ids = [manager.group_model.get(level=GroupLevelEnum.GUEST.value).id]
        for group_id in group_ids:
            user_group = manager.user_group_model()
            user_group.user_id = user.id
            user_group.group_id = group_id
            user_group_list.append(user_group)
        db.session.add_all(user_group_list)
    return Success("操作成功")


@admin_api.route("/group")
@permission_meta(name="查询所有分组及其权限", module="管理员", mount=False)
@admin_required
def get_admin_groups():
    start, count = paginate()
    groups = (
        manager.group_model.query.filter(
            manager.group_model.level != GroupLevelEnum.ROOT.value
        )
        .offset(start)
        .limit(count)
        .all()
    )
    if groups is None:
        raise NotFound("不存在任何分组")

    for group in groups:
        permissions = manager.permission_model.select_by_group_id(group.id)
        setattr(group, "permissions", permissions)
        group._fields.append("permissions")

    # hide root group
    total = (
        db.session.query(func.count(manager.group_model.id))
        .filter(
            manager.group_model.level != GroupLevelEnum.ROOT.value,
            manager.group_model.delete_time == None,
        )
        .scalar()
    )
    total_page = math.ceil(total / count)
    page = get_page_from_query()

    return {
        "count": count,
        "items": groups,
        "page": page,
        "total": total,
        "total_page": total_page,
    }


@admin_api.route("/group/all")
@permission_meta(name="查询所有分组", module="管理员", mount=False)
@admin_required
def get_all_group():
    groups = manager.group_model.query.filter(
        manager.group_model.delete_time == None,
        manager.group_model.level != GroupLevelEnum.ROOT.value,
    ).all()
    if groups is None:
        raise NotFound("不存在任何分组")
    return groups


@admin_api.route("/group/<int:gid>")
@permission_meta(name="查询一个分组及其权限", module="管理员", mount=False)
@admin_required
def get_group(gid):
    group = manager.group_model.get(id=gid, one=True, soft=False)
    if group is None:
        raise NotFound("分组不存在")
    permissions = manager.permission_model.select_by_group_id(gid)
    setattr(group, "permissions", permissions)
    group._fields.append("permissions")
    return group


@admin_api.route("/group", methods=["POST"])
@permission_meta(name="新建分组", module="管理员", mount=False)
@Logger(template="管理员新建了一个分组")  # add log
@admin_required
def create_group():
    form = NewGroup().validate_for_api()
    exists = manager.group_model.get(name=form.name.data)
    if exists:
        raise Forbidden("分组已存在，不可创建同名分组")
    with db.auto_commit():
        group = manager.group_model.create(
            name=form.name.data,
            info=form.info.data,
        )
        db.session.flush()
        group_permission_list = list()
        for permission_id in form.permission_ids.data:
            gp = manager.group_permission_model()
            gp.group_id = group.id
            gp.permission_id = permission_id
            group_permission_list.append(gp)
        db.session.add_all(group_permission_list)
    return Success("新建分组成功")


@admin_api.route("/group/<int:gid>", methods=["PUT"])
@permission_meta(name="更新一个分组", module="管理员", mount=False)
@admin_required
def update_group(gid):
    form = UpdateGroup().validate_for_api()
    exists = manager.group_model.get(id=gid)
    if not exists:
        raise NotFound("分组不存在，更新失败")
    exists.update(name=form.name.data, info=form.info.data, commit=True)
    return Success("更新分组成功")


@admin_api.route("/group/<int:gid>", methods=["DELETE"])
@permission_meta(name="删除一个分组", module="管理员", mount=False)
@Logger(template="管理员删除一个分组")  # add log
@admin_required
def delete_group(gid):
    exist = manager.group_model.get(id=gid)
    if not exist:
        raise NotFound("分组不存在，删除失败")
    guest_group = manager.group_model.get(level=GroupLevelEnum.GUEST.value)
    root_group = manager.group_model.get(level=GroupLevelEnum.ROOT.value)
    if gid in (guest_group.id, root_group.id):
        raise Forbidden("不可删除此分组")
    if manager.user_model.select_page_by_group_id(gid, root_group.id):
        raise Forbidden("分组下存在用户，不可删除")
    with db.auto_commit():
        manager.group_permission_model.query.filter_by(group_id=gid).delete(
            synchronize_session=False
        )
        exist.delete()
    return Success("删除分组成功")


@admin_api.route("/permission/dispatch", methods=["POST"])
@permission_meta(name="分配单个权限", module="管理员", mount=False)
@admin_required
def dispatch_auth():
    form = DispatchAuth().validate_for_api()
    one = manager.group_permission_model.get(
        group_id=form.group_id.data, permission_id=form.permission_id.data
    )
    if one:
        raise Forbidden("已有权限，不可重复添加")
    manager.group_permission_model.create(
        group_id=form.group_id.data, permission_id=form.permission_id.data, commit=True
    )
    return Success("添加权限成功")


@admin_api.route("/permission/dispatch/batch", methods=["POST"])
@permission_meta(name="分配多个权限", module="管理员", mount=False)
@admin_required
def dispatch_auths():
    form = DispatchAuths().validate_for_api()
    with db.auto_commit():
        for permission_id in form.permission_ids.data:
            one = manager.group_permission_model.get(
                group_id=form.group_id.data, permission_id=permission_id
            )
            if not one:
                manager.group_permission_model.create(
                    group_id=form.group_id.data,
                    permission_id=permission_id,
                )
    return Success("添加权限成功")


@admin_api.route("/permission/remove", methods=["POST"])
@permission_meta(name="删除多个权限", module="管理员", mount=False)
@admin_required
def remove_auths():
    form = RemoveAuths().validate_for_api()

    with db.auto_commit():
        db.session.query(manager.group_permission_model).filter(
            manager.group_permission_model.permission_id.in_(form.permission_ids.data),
            manager.group_permission_model.group_id == form.group_id.data,
        ).delete(synchronize_session=False)

    return Success("删除权限成功")

"""
    :copyright: © 2020 by the Lin team.
    :license: MIT, see LICENSE for more details.
"""
from lin import manager
from lin.db import db
from lin.enums import GroupLevelEnum


def init(force=False):
    db.create_all()
    if force:
        db.drop_all()
        db.create_all()
    elif (
        manager.user_model.get(one=False)
        or manager.user_group_model.get(one=False)
        or manager.group_model.get(one=False)
    ):
        exit("表中存在数据，初始化失败")
    with db.auto_commit():
        # create a super user group
        root_group = manager.group_model()
        root_group.name = "Root"
        root_group.info = "超级用户组"
        root_group.level = GroupLevelEnum.ROOT.value
        db.session.add(root_group)
        # create root user
        root = manager.user_model()
        root.username = "root"
        db.session.add(root)
        db.session.flush()
        root.password = "123456"
        # add relationships to db
        user_group = manager.user_group_model()
        user_group.user_id = root.id
        user_group.group_id = root_group.id
        db.session.add(user_group)
        # set default group as guest
        guest_group = manager.group_model()
        guest_group.name = "Guest"
        guest_group.info = "游客组"
        guest_group.level = GroupLevelEnum.GUEST.value
        db.session.add(guest_group)
        # initialize
        manager.sync_permissions()

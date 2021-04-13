"""
    :copyright: © 2020 by the Lin team.
    :Copyright (c) 2021 Chen Yang, Siqi Zhu,Jeffrey Li,Minyi Lei
    :license: MIT, see LICENSE for more details.
"""
import re
import time

from lin import manager
from lin.exception import ParameterError
from lin.form import Form
from wtforms import DateTimeField, FieldList, IntegerField, PasswordField, StringField
from wtforms.validators import DataRequired, EqualTo, NumberRange, Regexp, length

# registration check


class EmailForm(Form):
    email = StringField("电子邮件")

    def validate_email(self, value):
        if value.data:
            if not re.match(
                r"^[a-zA-Z0-9_.-]+@[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)*\.[a-zA-Z0-9]{2,6}$",
                value.data,
            ):
                raise ParameterError("电子邮箱不符合规范，请输入正确的邮箱")


class RegisterForm(EmailForm):
    password = PasswordField(
        "新密码",
        validators=[
            DataRequired(message="新密码不可为空"),
            Regexp(r"^[A-Za-z0-9_*&$#@]{6,22}$", message="密码长度必须在6~22位之间，包含字符、数字和 _ "),
            EqualTo("confirm_password", message="两次输入的密码不一致，请输入相同的密码"),
        ],
    )
    confirm_password = PasswordField(
        "确认新密码", validators=[DataRequired(message="请确认密码")]
    )
    username = StringField(
        validators=[
            DataRequired(message="用户名不可为空"),
            length(min=2, max=10, message="用户名长度必须在2~10之间"),
        ]
    )
    group_ids = FieldList(
        IntegerField(
            "分组id",
            validators=[
                DataRequired(message="请输入分组id"),
                NumberRange(message="分组id必须大于0", min=1),
            ],
        )
    )

    def validate_group_ids(self, value):
        for group_id in value.data:
            if not manager.group_model.count_by_id(group_id):
                raise ParameterError("分组不存在")


# login check


class LoginForm(Form):
    username = StringField(validators=[DataRequired()])
    password = PasswordField("密码", validators=[DataRequired(message="密码不可为空")])


# reset password check
class ResetPasswordForm(Form):
    new_password = PasswordField(
        "新密码",
        validators=[
            DataRequired(message="新密码不可为空"),
            Regexp(r"^[A-Za-z0-9_*&$#@]{6,22}$", message="密码长度必须在6~22位之间，包含字符、数字和 _ "),
            EqualTo("confirm_password", message="两次输入的密码不一致，请输入相同的密码"),
        ],
    )
    confirm_password = PasswordField(
        "确认新密码", validators=[DataRequired(message="请确认密码")]
    )


# change password check
class ChangePasswordForm(ResetPasswordForm):
    old_password = PasswordField("原密码", validators=[DataRequired(message="不可为空")])


# create new group
class NewGroup(Form):
    name = StringField(validators=[DataRequired(message="请输入分组名称")])
    info = StringField()
    # group permission
    permission_ids = FieldList(
        IntegerField(
            "权限id",
            validators=[
                DataRequired(message="请输入权限id"),
                NumberRange(message="权限id必须大于0", min=1),
            ],
        )
    )

    def validate_permission_id(self, value):
        exists = manager.permission_model.get(id=value.data)
        if not exists:
            raise ParameterError("权限不存在")


# update group info
class UpdateGroup(Form):
    name = StringField(validators=[DataRequired(message="请输入分组名称")])
    info = StringField()


class DispatchAuths(Form):
    # assign user permission
    group_id = IntegerField(
        "分组id",
        validators=[
            DataRequired(message="请输入分组id"),
            NumberRange(message="分组id必须大于0", min=1),
        ],
    )

    permission_ids = FieldList(
        IntegerField(validators=[DataRequired(message="请输入permission_ids字段")])
    )


class DispatchAuth(Form):
    # assign user permission
    group_id = IntegerField(
        "分组id",
        validators=[
            DataRequired(message="请输入分组id"),
            NumberRange(message="分组id必须大于0", min=1),
        ],
    )
    permission_id = IntegerField(
        validators=[DataRequired(message="请输入permission_id字段")]
    )


# batch remove permissions
class RemoveAuths(Form):
    group_id = IntegerField(
        "分组id",
        validators=[
            DataRequired(message="请输入分组id"),
            NumberRange(message="分组id必须大于0", min=1),
        ],
    )
    permission_ids = FieldList(
        IntegerField(validators=[DataRequired(message="请输入permission_ids字段")])
    )


class LogFindForm(Form):
    name = StringField()
    # 2018-11-01 09:39:35
    start = DateTimeField(validators=[])
    end = DateTimeField(validators=[])

    def validate_start(self, value):
        if value.data:
            try:
                _ = time.strptime(value.data, "%Y-%m-%d %H:%M:%S")
            except ParameterError as e:
                raise e

    def validate_end(self, value):
        if value.data:
            try:
                _ = time.strptime(value.data, "%Y-%m-%d %H:%M:%S")
            except ParameterError as e:
                raise e


class EventsForm(Form):
    group_id = IntegerField(
        "分组id",
        validators=[
            DataRequired(message="请输入分组id"),
            NumberRange(message="分组id必须大于0", min=1),
        ],
    )
    events = FieldList(StringField(validators=[DataRequired(message="请输入events字段")]))


# update user email
class UpdateInfoForm(EmailForm):
    nickname = StringField()
    avatar = StringField()

    def validate_nickname(self, value):
        if value.data:
            length = len(value.data)
            if length < 2 or length > 10:
                raise ParameterError("昵称长度必须在2~10之间")


# update user info
class UpdateUserInfoForm(EmailForm):
    group_ids = FieldList(
        IntegerField(
            "分组id",
            validators=[
                DataRequired(message="请输入分组id"),
                NumberRange(message="分组id必须大于0", min=1),
            ],
        )
    )

    def validate_group_ids(self, value):
        for group_id in value.data:
            if not manager.group_model.count_by_id(group_id):
                raise ParameterError("分组不存在")


class BookSearchForm(Form):
    q = StringField(validators=[DataRequired(message="必须传入搜索关键字")])


class CreateOrUpdateBookForm(Form):
    title = StringField(validators=[DataRequired(message="必须传入图书名")])
    author = StringField(validators=[DataRequired(message="必须传入图书作者")])
    summary = StringField(validators=[DataRequired(message="必须传入图书综述")])
    image = StringField(validators=[DataRequired(message="必须传入图书插图")])

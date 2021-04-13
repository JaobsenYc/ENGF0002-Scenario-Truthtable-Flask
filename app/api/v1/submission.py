"""
    a standard CRUD template of quiz
    通过 测试 来实现一套标准的 CRUD 功能，供学习
    :copyright: © 2020 by the Lin team.
    :license: MIT, see LICENSE for more details.
"""

from flask import g, request, jsonify
from lin import permission_meta
from lin.apidoc import DocResponse, api
from lin.exception import Success
from lin.jwt import group_required, login_required
from lin.redprint import Redprint
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    get_current_user,
    get_jwt_identity,
    verify_jwt_refresh_token_in_request,
)
from app.exception.api import QuizNotFound, StrIndexError
from app.model.v1.submission import Submission
from app.validator.schema import (
    AuthorizationSchema,
    QuizInSchema,
    QuizOutSchema,
    QuizQuerySearchSchema,
    QuizSchemaList,
)
from lin.db import db

submission_api = Redprint("submission")


@submission_api.route("/<int:id>")
# @api.validate(
#     resp=DocResponse(QuizNotFound, r=QuizOutSchema),
#     tags=["测试"],
# )
def get_quiz(id):
    """
    获取id指定测试的信息
    """
    submission = Submission.get(id=id)
    if submission:
        return submission
    raise QuizNotFound


@submission_api.route("")
# @api.validate(
#     resp=DocResponse(r=QuizSchemaList),
#     tags=["测试"],
# )
def get_quizs():
    """
    获取测试列表
    """
    return Submission.get(one=False)


@submission_api.route("/search")
# @api.validate(
#     query=QuizQuerySearchSchema,
#     resp=DocResponse(r=QuizSchemaList),
#     tags=["测试"],
# )
def search():
    """
    关键字搜索测试
    """
    return Submission.query.filter(
        Submission.title.like("%" + g.q + "%"), Submission.delete_time == None
    ).all()


@submission_api.route("", methods=["POST"])
# @api.validate(
#     headers=AuthorizationSchema,
#     json=QuizInSchema,
#     resp=DocResponse(Success(12)),
#     tags=["测试"],
# )
@login_required
def create_quiz():
    """
    创建测试
    """
    user = get_current_user()
    with db.auto_commit():
        # 添加书籍
        book1 = Submission()
        book1.expression = request.args.get("expression")
        book1.user_id=user.id
        print(book1.expression)
        db.session.add(book1)
    # Submission.create(book1, commit=True)
    return Success(12)


@submission_api.route("/<int:id>", methods=["PUT"])
@login_required
# @api.validate(
#     headers=AuthorizationSchema,
#     json=QuizInSchema,
#     resp=DocResponse(Success(13)),
#     tags=["测试"],
# )
def update_quiz(id):
    """
    更新测试信息
    """
    quiz_schema = request.context.json
    quiz = Submission.get(id=id)
    if quiz:
        quiz.update(
            id=id,
            **quiz_schema.dict(),
            commit=True,
        )
        return Success(13)
    raise QuizNotFound


@submission_api.route("/<int:id>", methods=["DELETE"])
# @permission_meta(name="删除测试", module="测试")
# @group_required
# @api.validate(
#     headers=AuthorizationSchema,
#     resp=DocResponse(QuizNotFound, Success(14)),
#     tags=["测试"],
# )
def delete_quiz(id):
    """
    传入id删除对应测试
    """
    submission = Submission.get(id=id)
    if submission:
        # 删除测试，软删除
        submission.delete(commit=True)
        return Success(14)
    raise QuizNotFound

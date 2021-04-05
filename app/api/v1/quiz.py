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

from app.exception.api import quizNotFound, StrIndexError
from app.model.v1.quiz import quiz
from app.validator.schema import (
    AuthorizationSchema,
    quizInSchema,
    quizOutSchema,
    quizQuerySearchSchema,
    quizSchemaList,
)

quiz_api = Redprint("quiz")


@quiz_api.route("/<int:id>")
@api.validate(
    resp=DocResponse(quizNotFound, r=quizOutSchema),
    tags=["测试"],
)
def get_quiz(id):
    """
    获取id指定测试的信息
    """
    quiz = quiz.get(id=id)
    if quiz:
        return quiz
    raise quizNotFound


@quiz_api.route("")
@api.validate(
    resp=DocResponse(r=quizSchemaList),
    tags=["测试"],
)
def get_quizs():
    """
    获取测试列表
    """
    return quiz.get(one=False)


@quiz_api.route("/search")
@api.validate(
    query=quizQuerySearchSchema,
    resp=DocResponse(r=quizSchemaList),
    tags=["测试"],
)
def search():
    """
    关键字搜索测试
    """
    return quiz.query.filter(
        quiz.title.like("%" + g.q + "%"), quiz.delete_time == None
    ).all()


@quiz_api.route("", methods=["POST"])
@login_required
@api.validate(
    headers=AuthorizationSchema,
    json=quizInSchema,
    resp=DocResponse(Success(12)),
    tags=["测试"],
)
def create_quiz():
    """
    创建测试
    """
    quiz_schema = request.context.json
    quiz.create(**quiz_schema.dict(), commit=True)
    return Success(12)


@quiz_api.route("/<int:id>", methods=["PUT"])
@login_required
@api.validate(
    headers=AuthorizationSchema,
    json=quizInSchema,
    resp=DocResponse(Success(13)),
    tags=["测试"],
)
def update_quiz(id):
    """
    更新测试信息
    """
    quiz_schema = request.context.json
    quiz = quiz.get(id=id)
    if quiz:
        quiz.update(
            id=id,
            **quiz_schema.dict(),
            commit=True,
        )
        return Success(13)
    raise quizNotFound


@quiz_api.route("/<int:id>", methods=["DELETE"])
@permission_meta(name="删除测试", module="测试")
@group_required
@api.validate(
    headers=AuthorizationSchema,
    resp=DocResponse(quizNotFound, Success(14)),
    tags=["测试"],
)
def delete_quiz(id):
    """
    传入id删除对应测试
    """
    quiz = quiz.get(id=id)
    if quiz:
        # 删除测试，软删除
        quiz.delete(commit=True)
        return Success(14)
    raise quizNotFound




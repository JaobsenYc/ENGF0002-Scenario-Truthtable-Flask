"""
    a standard CRUD template of quiz
    :copyright: © 2020 by the Lin team.
    :Copyright (c) 2021 Chen Yang, Siqi Zhu,Jeffrey Li,Minyi Lei
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
def get_quiz(id):
    """
    get quiz by querying id
    """
    submission = Submission.get(id=id)
    if submission:
        return submission
    raise QuizNotFound


@submission_api.route("")
def get_quizs():
    """
    get quiz list
    """
    return Submission.get(one=False)


@submission_api.route("/search")
# @api.validate(
#     query=QuizQuerySearchSchema,
#     resp=DocResponse(r=QuizSchemaList),
#     tags=["测试"],
# )
def search():
    return Submission.query.filter(
        Submission.title.like("%" + g.q + "%"), Submission.delete_time == None
    ).all()


@submission_api.route("", methods=["POST"])
@login_required
def create_quiz():
    """
    create quiz
    """
    user = get_current_user()
    with db.auto_commit():
        # add a book
        book1 = Submission()
        book1.expression = request.args.get("expression")
        book1.user_id=user.id
        print(book1.expression)
        db.session.add(book1)
    return Success(12)


@submission_api.route("/<int:id>", methods=["PUT"])
@login_required
def update_quiz(id):
    """
    update quiz info
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
def delete_quiz(id):
    """
    delete quiz by using id
    """
    submission = Submission.get(id=id)
    if submission:
        # soft delete
        submission.delete(commit=True)
        return Success(14)
    raise QuizNotFound

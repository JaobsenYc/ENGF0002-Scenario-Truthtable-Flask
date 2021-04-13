"""
    a standard CRUD template of quiz
    通过 测试 来实现一套标准的 CRUD 功能，供学习
    :copyright: © 2020 by the Lin team.
    :license: MIT, see LICENSE for more details.
"""
from app.model.lin import User as LinUser
from flask import g, request, jsonify
from lin.exception import Success
from lin.jwt import group_required, login_required
from lin.redprint import Redprint
from app.model.lin.user import User
from app.exception.api import QuizNotFound, StrIndexError
from app.model.v1.quiz import Quiz
from lin.db import db

quiz_api = Redprint("quiz")


@quiz_api.route("/<int:id>")
def get_quiz(id):
    """
    获取id指定测试的信息
    """
    quiz = Quiz.get(id=id)
    if quiz:
        return quiz.expression
    raise QuizNotFound


@quiz_api.route("")
def get_quizs():
    return Quiz.get(one=False)


@quiz_api.route("/search")
def search():
    return Quiz.query.filter(
        Quiz.title.like("%" + g.q + "%"), Quiz.delete_time == None
    ).all()


@quiz_api.route("", methods=["POST"])
def create_quiz():
    """
    创建测试
    """
    all_stu = LinUser.count_all_student()
    with db.auto_commit():
        book1 = Quiz()
        book1.expression = request.json.get("expression")
        book1.average_grade = 0
        book1.already_submission=0
        book1.submission = "0/"+ str(all_stu)
        print(book1.expression)
        db.session.add(book1)
    return Success(12)


@quiz_api.route("/<int:id>", methods=["PUT"])
@login_required
def update_quiz(id):
    """
    更新测试信息
    """

    expression = request.json.get("expression")
    print(request.json)
    quiz = Quiz.get(id=id)
    if quiz:
        quiz.update(
            id=id,
            expression=expression,
            commit=True,
        )
        return Success(13)
    raise QuizNotFound


@quiz_api.route("/submission", methods=["GET"])
# @api.validate(
#     headers=AuthorizationSchema,
#     json=QuizInSchema,
#     resp=DocResponse(Success(13)),
#     tags=["测试"],
# )
def update_submission():
    id = request.args.get("id")
    score = float(request.args.get("score"))/100
    quiz = Quiz.get(id=id)
    al_sub = Quiz.get(id=id).already_submission
    av_grade = Quiz.get(id=id).average_grade
    all_stu = LinUser.count_all_student()
    if quiz:
        quiz.update(
            id=id,
            average_grade=(al_sub * av_grade + score) / (al_sub + 1),
            already_submission=al_sub + 1,
            submission=str(al_sub + 1) + "/" + str(all_stu),
            commit=True,
        )
        return Success(13)
    raise QuizNotFound


@quiz_api.route("/<int:id>", methods=["DELETE"])
def delete_quiz(id):
    quiz = Quiz.get(id=id)
    if quiz:
        quiz.delete(commit=True)
        return Success(14)
    raise QuizNotFound

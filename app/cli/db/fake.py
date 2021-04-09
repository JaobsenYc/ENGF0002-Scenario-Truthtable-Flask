"""
    :copyright: © 2020 by the Lin team.
    :license: MIT, see LICENSE for more details.
"""

from lin.db import db

from app.model.v1.quiz import Quiz


def fake():
    with db.auto_commit():
        # 添加书籍
        book1 = Quiz()
        book1.expression = "(a /\ !b /\ c)"
        book1.average_grade = 80
        book1.already_submission = 100
        book1.submission = "1/100"
        db.session.add(book1)


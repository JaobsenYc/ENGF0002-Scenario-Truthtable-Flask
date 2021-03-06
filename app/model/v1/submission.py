"""
    :copyright: © 2020 by the Lin team.
    :Copyright (c) 2021 Chen Yang, Siqi Zhu,Jeffrey Li,Minyi Lei

    :license: MIT, see LICENSE for more details.
"""

from lin.interface import InfoCrud as Base
from sqlalchemy import Column, Integer, String

from app.exception.api import QuizNotFound


class Submission(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, nullable=False)
    quiz_id = Column(Integer, nullable=False)
    score = Column(Integer, nullable=False)



    # title = Column(String(50), nullable=False)
    # author = Column(String(30), default="未名")
    # summary = Column(String(1000))
    # image = Column(String(100))

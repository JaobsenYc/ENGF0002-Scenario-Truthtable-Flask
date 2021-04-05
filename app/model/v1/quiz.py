"""
    :copyright: © 2020 by the Lin team.
    :license: MIT, see LICENSE for more details.
"""

from lin.interface import InfoCrud as Base
from sqlalchemy import Column, Integer, String

from app.exception.api import QuizNotFound


class Quiz(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    expression = Column(String(50))


    # title = Column(String(50), nullable=False)
    # author = Column(String(30), default="未名")
    # summary = Column(String(1000))
    # image = Column(String(100))

"""
    :copyright: © 2020 by the Lin team.
    :Copyright (c) 2021 Chen Yang, Siqi Zhu,Jeffrey Li,Minyi Lei
    :license: MIT, see LICENSE for more details.
"""

from lin.interface import InfoCrud as Base
from sqlalchemy import Column, Integer, String, Float


class Quiz(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    expression = Column(String(50))
    average_grade = Column(Float)
    already_submission = Column(Integer)
    submission = Column(String(50))





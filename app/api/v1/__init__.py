"""
    :copyright: © 2020 by the Lin team.
    :license: MIT, see LICENSE for more details.
"""

from flask import Blueprint

from app.api.v1 import quiz
from app.api.v1 import submission
from app.api.v1 import ttg
from app.api.v1 import truthtable
def create_v1():
    bp_v1 = Blueprint("v1", __name__)
    quiz.quiz_api.register(bp_v1)
    ttg.ttg_api.register(bp_v1)
    truthtable.truthtable_api.register(bp_v1)
    return bp_v1

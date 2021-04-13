"""
    :Copyright (c) 2021 Chen Yang, Siqi Zhu,Jeffrey Li,Minyi Lei
    :license: MIT, see LICENSE for more details.
"""

from flask import g, request, jsonify
from lin import permission_meta
from lin.apidoc import DocResponse, api
from lin.exception import Success
from lin.jwt import group_required, login_required
from lin.redprint import Redprint
from app.exception.api import QuizNotFound, StrIndexError

from app.truthtable.truthTable import *
from app.truthtable.main import *

truthtable_api = Redprint("truthtable")


@truthtable_api.route("/valid")
def valid():
    """
    Check validity of expreesion
    """
    expression = request.args.get("expression")
    parseTree = getParse(expression)

    return parseTree is not None


@truthtable_api.route("/truthtable")
def truthtable():
    """
    Return html format of truth table
    """
    expression = request.args.get("expression")
    parseTree = getParse(expression)
    truthGen = truthTable(parseTree)
    res = truthGen.generateTruth()

    return res


import json


@truthtable_api.route("/truthtable/correct")
def isCorrect():
    """
    Return boolean indicating correctness of submitted ans
    ans in the form of [True,False,False,False]
    """

    expression = request.args.get("expression")
    ans = request.args.get("ans")

    parseTree = getParse(expression)
    truthGen = truthTable(parseTree)

    res = truthGen.getResults()
    diff = 0
    print(res)
    try:
        if res != ans:
            for i in range(len(ans)):
                if ans[i] != res[i]:
                    diff += 1
    except IndexError:
        raise StrIndexError
    score = format((len(ans) - diff) / (len(ans)) * 100, '.2f')
    response = {'Correct': res == ans, 'Answer': res, 'Score': score}

    return jsonify(response)

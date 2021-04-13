from app.truthtable.truthTable import *
from app.truthtable.main import *
from flask import g, request, jsonify

from lin.redprint import Redprint

from app.exception.api import QuizNotFound, StrIndexError

ttg_api = Redprint("ttg")


@ttg_api.route("/valid")
def valid():
    """
    Check validity of expreesion
    """
    expression = request.args.get("expression")
    parseTree = getParse(expression)

    return parseTree is not None


@ttg_api.route("/truthtable_html")
def truthtable_html():
    """
    Return html format of truth table
    """
    # expression = request.args.get("expression")
    # parseTree = getParse(expression)
    # truthGen = truthTable(parseTree)
    # res = truthGen.generateTruth()
    expression = request.args.get("expression")
    parseTree = getParse(expression)
    truthGen = truthTable(parseTree)
    res = truthGen.generateTruthHtml()

    return res


@ttg_api.route("/truthtable_json")
def truthtable_json():
    """
    Return html format of truth table
    """
    # expression = request.args.get("expression")
    # parseTree = getParse(expression)
    # truthGen = truthTable(parseTree)
    # res = truthGen.generateTruth()
    expression = request.args.get("expression")
    quiz = request.args.get("quiz")
    print(quiz)
    if quiz is not None:
        parseTree = getParse(expression)
        truthGen = truthTable(parseTree)
        res = truthGen.generateTruthJson_quiz()
        return res
    else:
        parseTree = getParse(expression)
        truthGen = truthTable(parseTree)
        res = truthGen.generateTruthJson()
        return res


import json


@ttg_api.route("/truthtable/correct")
def isCorrect():
    """
    Return boolean indicating correctness of submitted ans
    ans in the form of [True,False,False,False]
    """

    expression = request.args.get("expression")
    ans = request.args.get("ans")
    quizid = request.args.get("quizid")
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

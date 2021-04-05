from app.truthtable.truthTable import *
from app.truthtable.main import *

ttg_api = Redprint("ttg")

@ttg_api.route("/valid")
def valid():
    """
    Check validity of expreesion
    """
    expression = request.args.get("expression")
    parseTree = getParse(expression)

    return parseTree is not None


@ttg_api.route("/truthtable")
def truthtable():
    """
    Return html format of truth table
    """
    expression = request.args.get("expression")
    parseTree = getParse(expression)
    truthGen = truthTable(parseTree)
    res = truthGen.generateTruth()

    return


import json


@ttg_api.route("/truthtable/correct")
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
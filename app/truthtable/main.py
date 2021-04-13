from app.truthtable.Lexer import Lexer
from app.truthtable.Parser import Parser
from app.truthtable.constants import *
from app.truthtable.truthTable import truthTable

parseTree = ""


def output(i):
    if i is None:
        print("Invalid input")
    else:
        print(i)


def getParse(text, debug=False):
    text = text.upper()
    lexer = Lexer(text)
    tokenstream = lexer.make_token()
    if tokenstream[0] != Invalid_Input:
        if debug:
            print(tokenstream)
        parser = Parser(tokenstream)
        parsed = parser.parse()
        return parsed
    else:
        return None


def getParseRun():
    while True:
        text = input("Enter a proposition: ")
        output(getParse(text))


def getParseDebug():
    t = "(a /\ !b /\ c)"
    print(t)
    a = getParse(t, True)
    output(a)


def goodParse(st):
    parseTree = getParse(st)
    if parseTree is None:
        return False
    return True

def run():
    parseTree = getParse("(a /\ !b /\ c)")
    if parseTree is None:
        print("Invalid")
    else:
        truthGen = truthTable(parseTree)
        print(truthGen.generateTruthJson_quiz())


if __name__ == "__main__":
    run()

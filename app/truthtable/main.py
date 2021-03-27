from Lexer import Lexer
from Parser import Parser
from constants import *
from truthTable import truthTable

parseTree = ""

def output(i):
    if i is None:
        print("Invalid input")
    else:
        print(i)

def getParse(text,debug = False):
    text= text.upper()
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
    a = getParse(t,True)
    output(a)

def goodParse(st):
    parseTree = getParse(st)
    if parseTree is None:
        return False
    return True

# def isCorrect(ans):
#     res = truthTable.getResults()
#     if res == ans:
#         return True
#     return False

def run():
    while True:
        parseTree = getParse(input("Enter a proposition: "))
        if parseTree is None:
            print("Invalid")
        else:
            truthGen = truthTable(parseTree)
            truthGen.generateTruth()

if __name__ == "__main__":
    #getParseDebug()
    run()

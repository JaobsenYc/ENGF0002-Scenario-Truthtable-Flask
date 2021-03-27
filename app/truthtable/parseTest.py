from app.truthtable.main import *


def test():
    flag = True
    failed = []
    with open("prop.txt") as f:
        for st in f:
            if not goodParse(st):
                failed.append(st)
                flag = False

    if not flag:
        print("Failed:")
        for fail in failed:
            print(fail)
    else:
        print("Success")


test()
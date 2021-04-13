import ttg
import prettytable
import pandas


class truthTable:
    def __init__(self, AST):
        self.AST = AST
        self.proposition = []
        self.propVar = []
        self.operations = ["and", "or", "=>", "~"]
        self.convertProposition()
        print(self.proposition)
        print(self.propVar)

    def convertProposition(self):
        treetoString = str(self.AST)
        print(treetoString)
        treetoString = treetoString.replace("CONJ", "and")
        treetoString = treetoString.replace("DISJ", "or")
        treetoString = treetoString.replace("IMPL", "=>")
        treetoString = treetoString.replace("BIMPL", "=")
        treetoString = treetoString.replace("NOT", "~")
        self.proposition.append(treetoString)
        li = treetoString.replace("(", "").replace(")", "").split()
        for element in li:
            if element not in self.operations and element not in self.propVar:
                self.propVar.append(element)

    def generateTruthHtml(self):
        truth = ttg.Truths(self.propVar, self.proposition, ints=False)

        ans = truth.as_tabulate(index=False, table_format='html')

        return ans

    def generateTruthJson(self):
        truth = ttg.Truths(self.propVar, self.proposition, ints=False)

        ans = pandas.DataFrame.to_json(truth.as_pandas())

        return ans

    def generateTruthJson_quiz(self):
        truth = ttg.Truths(self.propVar, self.proposition, ints=False)

        ans = truth.as_pandas()
        ans.drop(columns=ans.columns[-1],
                 axis=1,
                 inplace=True)
        ans = pandas.DataFrame.to_json(ans)

        return ans

    def getResults(self):
        NgC = ttg.Truths(self.propVar, self.proposition, ints=True)
        res = NgC.as_pandas()[self.proposition].values.tolist()
        res = [str(i[0]) for i in res]
        res2 = "".join(res)

        return res2

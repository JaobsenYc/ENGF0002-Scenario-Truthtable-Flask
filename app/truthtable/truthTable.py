import ttg
import prettytable


class truthTable:
    def __init__(self,AST):
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
        treetoString = treetoString.replace("CONJ","and")
        treetoString = treetoString.replace("DISJ", "or")
        treetoString = treetoString.replace("IMPL", "=>")
        treetoString = treetoString.replace("BIMPL", "=")
        treetoString = treetoString.replace("NOT", "~")
        self.proposition.append(treetoString)
        li = treetoString.replace("(","").replace(")","").split()
        for element in li:
            if element not in self.operations and element not in self.propVar:
                self.propVar.append(element)

    def generateTruth(self):
        #print(ttg.Truths(['p','q','r'],['(p or (~q)) => r'],ints=False))
        #print(ttg.Truths(self.propVar, self.proposition, ints=False))
        truth = ttg.Truths(self.propVar, self.proposition, ints=False)
        ans = truth.as_tabulate(index=False, table_format='html')

        return ans
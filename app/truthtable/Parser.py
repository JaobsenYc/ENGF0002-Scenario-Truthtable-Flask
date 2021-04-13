from app.truthtable.constants import *


class varNode:
    def __init__(self, var):
        self.var = var


    def isFailed(self):
        return False

    def __repr__(self):
        return f"{self.var}"


class BinNode:
    def __init__(self, l, r, op):
        self.l = l
        self.r = r
        self.op = op
        self.successParse = True
        if self.l is None or self.r is None or self.l.isFailed() or self.r.isFailed():
            self.failedParse()

    def failedParse(self):
        self.successParse = False

    def isFailed(self):
        return not self.successParse

    def __repr__(self):
        return f"({self.l} {self.op} {self.r})"


class NotNode:
    def __init__(self, arg, op):
        self.arg = arg
        self.op = op
        self.successParse = True
        if arg is None:
            self.failedParse()

    def failedParse(self):
        self.successParse = False

    def isFailed(self):
        return not self.successParse

    def __repr__(self):
        return f"({self.op} {self.arg})"


class Parser:
    def __init__(self, token_stream):
        self.token_stream = token_stream
        self.pos = -1
        self.current_lexeme = None
        self.nextLex()

    def nextLex(self):
        self.pos += 1
        if self.pos < len(self.token_stream):
            self.current_lexeme = self.token_stream[self.pos]
        return self.current_lexeme

    def recurseExp(self):
        self.nextLex()
        newProp = self.proposition()
        self.nextLex()
        if self.current_lexeme.type == RPAREN:
            self.nextLex()
            return newProp
        elif self.current_lexeme.type in operations:
            return newProp
        else:
            return None

    def Variable(self):
        lex = self.current_lexeme
        if lex.type == NOT:
            self.nextLex()
            if self.current_lexeme.type == LPAREN:
                var = self.recurseExp()
            else:
                var = self.current_lexeme
            ret = NotNode(var,lex)
            return ret
        elif lex.type == VAR:
            self.nextLex()
            return varNode(lex)
        elif lex.type == LPAREN:
            return self.recurseExp()

    def binOp(self, arg, operation):
        leftNode = arg()
        while self.current_lexeme.type in operation:
            op = self.current_lexeme
            self.nextLex()
            rightNode = arg()
            leftNode = BinNode(leftNode, rightNode, op)
        return leftNode

    def Conjunction(self):
        return self.binOp(self.Variable, CONJ)

    def Disjunction(self):
        return self.binOp(self.Conjunction, DISJ)

    def proposition(self):
        return self.binOp(self.Disjunction, (IMPL, BIIMPL))

    def parse(self):
        try:
            result = self.proposition()
            if (isinstance(result,varNode)) or (isinstance(result,NotNode)):
                return result
            elif result.l.isFailed() or result.r.isFailed():
                return None
            return result
        except AttributeError as e:
            return None

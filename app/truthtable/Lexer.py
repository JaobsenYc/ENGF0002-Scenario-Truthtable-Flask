from app.truthtable.constants import *


class Token:
    def __init__(self, tok_type, value=None):
        self.type = tok_type
        self.value = value

    def __repr__(self):
        if self.value:
            return f"{self.value}"
        return f"{self.type}"


class Lexer:
    def __init__(self, char_stream):
        self.char_stream = char_stream.upper()
        self.pos = -1
        self.current_char = None
        self.next()

    def expected_next(self, next, steps=2):
        virt_next = self.char_stream[self.pos + 1] if self.pos + 1 < len(self.char_stream) else None
        if virt_next == next:
            for x in range(steps):
                self.next()
            return 1

    def next(self):
        self.pos += 1
        self.current_char = self.char_stream[self.pos] if self.pos < len(self.char_stream) else None

    def error(self):
        self.next()
        return [Invalid_Input]

    def make_token(self):
        tokens = []
        while self.current_char is not None:
            if self.current_char in " \n":
                self.next()
            elif self.current_char in alphabet:
                tokens.append(Token(VAR, self.current_char))
                self.next()
            elif self.current_char in "~!":
                tokens.append(Token(NOT))
                self.next()
            elif self.current_char == "/":
                if self.expected_next("\\"):
                    tokens.append(Token(CONJ))
                else:
                    return self.error()
            elif self.current_char == "\\":
                if self.expected_next("/"):
                    tokens.append(Token(DISJ))
                else:
                    return self.error()
            elif self.current_char == "-":
                if self.expected_next(">"):
                    tokens.append(Token(IMPL))
                else:
                    return self.error()
            elif self.current_char == "<":
                if self.expected_next("-", 1):
                    if self.expected_next(">", 1):
                        tokens.append(Token(BIIMPL))
                        self.next()
                    else:
                        return self.error()
                else:
                    return self.error()
            elif self.current_char == "(":
                tokens.append(Token(LPAREN))
                self.next()
            elif self.current_char == ")":
                tokens.append(Token(RPAREN))
                self.next()
            else:
                return self.error()

        if tokens[0].type != LPAREN:
            tokens.insert(0,Token(LPAREN))
        if tokens[-1].type != RPAREN:
            tokens.append(Token(RPAREN))
        return tokens


if __name__ == "__main__":
    def run(char_stream):
        lex = Lexer(char_stream)
        tokens = lex.make_token()
        return tokens


    while True:
        st = input("Enter a proposition: ")
        result = run(st)
        print(result)

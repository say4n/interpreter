"""Test program
"""

from parser import Parser
from lexer import Lexer

def main():
    while True:
        try:
            text = input('calc> ')
        except EOFError:
            break
        if not text:
            break
        lexer = Lexer(text)
        interpreter = Parser(lexer)
        result = interpreter.expr()
        print(result)


if __name__ == "__main__":
    main()

"""Test program
"""

from parser import Parser
from lexer import Lexer
from interpreter import Interpreter

def main():
    while True:
        try:
            text = input('calc> ')
        except EOFError:
            break
        if not text:
            break
        
        lexer = Lexer(text)
        parser = Parser(lexer)
        interpreter = Interpreter(parser)
        
        result = interpreter.interpret()
        
        print(result)


if __name__ == "__main__":
    main()

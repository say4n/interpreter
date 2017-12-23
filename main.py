"""Test program
"""

from parser import Parser
from lexer import Lexer
from interpreter import Interpreter, PostfixNotation, PrefixNotation

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


        lexer = Lexer(text)
        parser = Parser(lexer)
        postfix = PostfixNotation(parser)
        
        result = postfix.translate()
        print("postfix: " + result)


        lexer = Lexer(text)
        parser = Parser(lexer)
        prefix = PrefixNotation(parser)
        
        result = prefix.translate()
        print("prefix: " + result)


if __name__ == "__main__":
    main()

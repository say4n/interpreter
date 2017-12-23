"""Tokenizer
"""

from token_types import *

class Token:
    """Token 
    """
    def __init__(self, _type, _value):
        self.type = _type
        self.value = _value

    def __str__(self):
        return 'Token({type}, {value})'.format(
            type=self.type,
            value=repr(self.value)
        )

    def __repr__(self):
        return self.__str__()


class Lexer:
    """Lexical analyzer
    """
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_char = self.text[self.pos]

    def advance(self):
        # Increment `pos` pointer
        self.pos += 1
        if self.pos > len(self.text) - 1:
            self.current_char = None 
        else:
            self.current_char = self.text[self.pos]

    def skip_whitespace(self):
        # Ignore whitespace
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def integer(self):
        # Return a (multidigit) integer consumed from the input
        num = ""
        while self.current_char is not None and self.current_char.isdigit():
            num += self.current_char
            self.advance()
        
        return int(num)

    def get_next_token(self):
        # Get the next token
        if self.current_char is None:
            return Token(EOF, None)

        if self.current_char.isspace():
            self.skip_whitespace()

        if self.pos >= len(self.text):
            return Token(EOF, None)

        if self.current_char.isdigit():
            token = Token(INTEGER, self.integer())
            
            return token

        if self.current_char == '+':
            self.advance()
            
            return Token(PLUS, '+')

        if self.current_char == '-':
            self.advance()
            
            return Token(MINUS, '-')

        if self.current_char == '*':
            self.advance()
            
            return Token(MUL,'*')

        if self.current_char == '/':
            self.advance()
            
            return Token(DIV, '/')

        if self.current_char == '^':
            self.advance()
            
            return Token(POW, '^')

        if self.current_char == '(':
            self.advance()
            
            return Token(LPAREN, '(')

        if self.current_char == ')':
            self.advance()
            
            return Token(RPAREN, ')')

        self._error()

    def _error(self):
        raise Exception('Error tokenizing input')

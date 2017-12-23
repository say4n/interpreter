"""Parser
"""

from token_types import *
from ast import *

class Parser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()

    def _error(self):
        raise Exception('Error parsing input')

    def eat(self, token_type):
        """Consume `self.current_token`
        """
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token()
        
        else:
            self._error()

    def factor(self):
        """(PLUS | MINUS) factor | INTEGER | LPAREN expr RPAREN
        """
        token = self.current_token
        
        if token.type == PLUS:
            self.eat(PLUS)
            return UnaryOp(token, self.factor())

        elif token.type == MINUS:
            self.eat(MINUS)
            return UnaryOp(token, self.factor())

        elif token.type == INTEGER:
            self.eat(INTEGER)
            return Num(token)
        
        elif token.type == LPAREN:
            self.eat(LPAREN)
            node = self.expr()
            self.eat(RPAREN)

            return node

    def term(self):
        """term   : factor ((MUL | DIV | POW) factor)*
        """
        node = self.factor()

        while self.current_token.type in (MUL, DIV, POW):
            token = self.current_token

            if token.type == MUL:
                self.eat(MUL)
            
            elif token.type == DIV:
                self.eat(DIV)
            
            elif token.type == POW:
                self.eat(POW)

            node = BinOp(left=node, op=token, right=self.factor())

        return node


    def expr(self):
        """Arithmetic expression parser / interpreter

        expr   : term ((PLUS | MINUS) term)*
        term   : factor ((MUL | DIV | POW) factor)*
        factor : (PLUS | MINUS) factor | INTEGER | LPAREN expr RPAREN
        """
        node = self.term()

        while self.current_token.type in (PLUS, MINUS):
            token = self.current_token

            if token.type == PLUS:
                self.eat(PLUS)
            
            elif token.type == MINUS:
                self.eat(MINUS)

            node = BinOp(left=node, op=token, right=self.term())
        
        return node

    def parse(self):
        return self.expr()

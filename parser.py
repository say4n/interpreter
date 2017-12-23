"""Parser
"""

from token_types import *

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
        """factor : INTEGER | LPAREN expr RPAREN
        """
        token = self.current_token
        
        if token.type == INTEGER:
            self.eat(INTEGER)
            return token.value
        
        elif token.type == LPAREN:
            self.eat(LPAREN)
            result = self.expr()
            self.eat(RPAREN)

            return result

    def term(self):
        """term   : factor ((MUL | DIV | POW) factor)*
        """
        result = self.factor()

        while self.current_token.type in (MUL, DIV, POW):
            token = self.current_token

            if token.type == MUL:
                self.eat(MUL)
                result = result * self.factor()
            
            elif token.type == DIV:
                self.eat(DIV)
                result = result // self.factor()
            
            elif token.type == POW:
                self.eat(POW)
                result = result ** self.factor()

        return result


    def expr(self):
        """Arithmetic expression parser / interpreter

        expr   : term ((PLUS | MINUS) term)*
        term   : factor ((MUL | DIV | POW) factor)*
        factor : INTEGER | LPAREN expr RPAREN
        """
        result = self.term()

        while self.current_token.type in (PLUS, MINUS):
            token = self.current_token

            if token.type == PLUS:
                self.eat(PLUS)
                result = result + self.term()
            
            elif token.type == MINUS:
                self.eat(MINUS)
                result = result - self.term()
        
        return result

    def parse(self):
        return self.expr()

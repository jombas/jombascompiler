from pymjc.front.lexer import MJLexer
from sly import Parser

class MJParser(Parser):

    def __init__(self):
        self.syntax_error = False
        self.debugfile = 'parser.out'
        super().__init__
                         
    tokens = MJLexer.tokens

    syntax_error = False

    debugfile = 'parser.out'

    #TODO - Write your grammar here
    class BinOp(object):
        def __init__(self, op, left, right):
            self.op = op
            self.left = left
            self.right = right

    class Identifier(object):
        def __init__(self, value):
            self.value = value
            
    @_('ID')
    def id(self, p):
        return Identifier(p[0])
        

'''
    @_(expr DOT LENGTH)
    def expr(self, p):
        placeholder
'''
    def error(self, p):
        self.syntax_error = True

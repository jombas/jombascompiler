import lex


class CalcLexer(lex.Lexer): #lembrar de tirar!!!!!!!!
    # Set of token names.   This is always required
    tokens = { NUMBER, ID, NUMBERVEC,WHILE, IF, ELSE, INT, LENGHT
               PLUS, MINUS, TIMES, DIVIDE, ASSIGN,
               EQ, LT, LE, GT, GE, NE,
               PUBLIC, STATIC, VOID, MAIN,
               CLASS, EXTENDS, RETURN
               
               }


    literals = { '(', ')', '{', '}', ';' ,'.', '?','*',',','!'} #perguntar do ponto para o lincon

    # String containing ignored characters
    ignore = ' \t'

    # Regular expression rules for tokens
    PLUS    = r'\+'
    MINUS   = r'-'
    TIMES   = r'\*'
    DIVIDE  = r'/'
    EQ      = r'=='
    ASSIGN  = r'='
    LE      = r'<='
    LT      = r'<'
    GE      = r'>='
    GT      = r'>'
    NE      = r'!='
    

    @_(r'\d+')
    def NUMBER(self, t):
        t.value = int(t.value)
        return t


    NUMBERVEC = r''
    # Identifiers and keywords
    ID = r'[a-zA-Z_][a-zA-Z0-9_]*'

    ID['lenght'] = LENGHT
    ID['int'] = INT
    ID['if'] = IF
    ID['else'] = ELSE
    ID['while'] = WHILE
    ID['public'], ID['static'], ID['void'], ID['main'] = PUBLIC, STATIC, VOID, MAIN 
    ID['class'] = CLASS
    ID['extends'] = EXTENDS


    ignore_comment = r'\#.*'

    # Line number tracking
    @_(r'\n+')
    def ignore_newline(self, t):
        self.lineno += t.value.count('\n')

    def error(self, t):
        print('Line %d: Bad character %r' % (self.lineno, t.value[0]))
        self.index += 1

if __name__ == '__main__':
    data = '''
# Counting
x = 0;
while (x < 10) {
    System.out.println x:
    x = x + 1;
}
'''
    lexer = CalcLexer()
    for tok in lexer.tokenize(data):
        print(tok)
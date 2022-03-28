import lex


class CalcLexer(lex.Lexer): #lembrar de tirar!!!!!!!!
    # Set of token names.   This is always required
    tokens = { NUMBER, ID, NUMBERVEC,WHILE, IF, ELSE, INT, LENGTH, BOOLEAN,
               PLUS, MINUS, TIMES, LT, ASSIGN, AND,
               PUBLIC, STATIC, VOID, MAIN, PRINT,
               CLASS, EXTENDS, RETURN,
               BOOL
               #THIS, NEW
               #(operador * em headers, para nao confundir com o TIMES)
            # Operadores que não tem no mini java:
               # EQ, LE, GT, GE, NE, DIVIDE,
               }


    literals = { '(', ')', '{', '}', ';' ,'.', '?',',','!'} #perguntar do ponto e o * para o lincon

    # String containing ignored characters
    ignore  = ' \t'

    PRINT   = r'System.out.println' 

    # Regular expression rules for tokens
    PLUS    = r'\+'
    MINUS   = r'-'
    TIMES   = r'\*'
    #DIVIDE  = r'/'
    #EQ      = r'=='
    ASSIGN  = r'='
    #LE      = r'<='
    LT      = r'<'
    #GE      = r'>='
    #GT      = r'>'
    #NE      = r'!='
    AND     = r'&&'
    
    #operador * no header de classes e métodos deve ser implementado como expressão regular, talvez como r')\*'
    

    @_(r'\d+')
    def NUMBER(self, t):
        t.value = int(t.value)
        return t

    # adicionar um meio de não ser considerado um id e sim um boolean
    @_(r'true|false') 
    def BOOL(self, t):
        t.value = bool(t.value)
        return t

    
    #implementar o int[] e int[valor]
    NUMBERVEC = r'' 



    # Identifiers and keywords
    ID = r'[a-zA-Z_][a-zA-Z0-9_]*'

    ID['boolean'] = BOOLEAN
    ID['length'] = LENGTH
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
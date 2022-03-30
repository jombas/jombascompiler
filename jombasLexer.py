import lex


class CalcLexer(lex.Lexer): #lembrar de tirar!!!!!!!!
    # Set of token names.   This is always required
    tokens = { NUMBER, ID,WHILE, IF, ELSE, INT, LENGTH, BOOLEAN,
               PLUS, MINUS, TIMES, LT, ASSIGN, AND,
               PUBLIC, STATIC, VOID, MAIN, PRINT,
               CLASS, EXTENDS, RETURN,
               TRUE, FALSE,
               THIS, NEW
            # Operadores que não tem no mini java:
               # EQ, LE, GT, GE, NE, DIVIDE,
               }


    literals = { '(', ')', '{', '}', ';' ,'.',',','!','[',']'} #perguntar do ponto e o * para o lincon

    # String containing ignored characters
    ignore  = ' \t'

    PRINT   = r'System\.out\.println' 

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

    

    @_(r'\d+')
    def NUMBER(self, t):
        t.value = int(t.value)
        return t


    # Identifiers and keywords
    ID = r'[a-zA-Z_][a-zA-Z0-9_]*'

    ID['this'] = THIS
    ID['new'] = NEW
    ID['return'] = RETURN
    ID['true'] = TRUE
    ID['false'] = FALSE
    ID['boolean'] = BOOLEAN
    ID['length'] = LENGTH
    ID['int'] = INT
    ID['if'] = IF
    ID['else'] = ELSE
    ID['while'] = WHILE
    ID['public'], ID['static'], ID['void'], ID['main'] = PUBLIC, STATIC, VOID, MAIN 
    ID['class'] = CLASS
    ID['extends'] = EXTENDS


    ignore_comment = r'//.*'

    # Line number tracking
    @_(r'\n+')
    def ignore_newline(self, t):
        self.lineno += t.value.count('\n')

    def error(self, t):
        print('Line %d: Bad character %r' % (self.lineno, t.value[0]))
        self.index += 1

if __name__ == '__main__':
    data = '''
class Factorial{
    public static void main(String[] a){
	System.out.println(new Fac().ComputeFac(10));
    }
}

class Fac {

    public int ComputeFac(int num){
	int num_aux ;
	if (num < 1)
	    num_aux = 1 ;
	else 
	    num_aux = num * (this.ComputeFac(num-1)) ;
	return num_aux ;
    }

  }
'''
    lexer = CalcLexer()
    for tok in lexer.tokenize(data):
        print(tok)
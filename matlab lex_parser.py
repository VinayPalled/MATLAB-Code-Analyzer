from ply import lex, yacc
import sys

# List of tokens
tokens = (
    'ID',
    'EQUALS',
    'NUMBER',
    'FOR',
    'COLON',
    'END',
    'SEMICOLON',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'LBRACKET',
    'RBRACKET',
    'COMMA',
    'TABLE',
    'PLOT',
)

# Tokens
t_EQUALS = r'='
t_COLON = r':'
t_SEMICOLON = r';'
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_COMMA = r','
t_TABLE = r'table'
t_PLOT = r'plot'

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_FOR(t):
    r'for'
    return t

def t_END(t):
    r'end'
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    return t

t_ignore = ' \t'  # Ignore spaces and tabs

def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print("Invalid syntax")
    sys.exit()

lexer = lex.lex()

# Grammar rules
def p_assignment(p):
    'assignment : ID EQUALS expression SEMICOLON'
    pass

def p_expression(p):
    '''expression : ID
                  | NUMBER
                  | expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression
                  | LPAREN expression RPAREN
                  | table_expression
                  | table_creation
                  | plot_expression
                  | for_loop'''
    pass

def p_table_expression(p):
    'table_expression : LBRACKET table_content RBRACKET'
    pass

def p_table_content(p):
    '''table_content : table_row
                     | table_content SEMICOLON table_row'''
    pass

def p_table_row(p):
    'table_row : expression'
    pass

def p_table_creation(p):
    'table_creation : ID EQUALS TABLE LPAREN table_vars RPAREN SEMICOLON'
    pass

def p_table_vars(p):
    '''table_vars : table_vars COMMA expression
                  | expression'''
    pass

def p_plot_expression(p):
    'plot_expression : PLOT LPAREN expression COMMA expression RPAREN SEMICOLON'
    pass

def p_for_loop(p):
    'for_loop : FOR ID EQUALS NUMBER SEMICOLON for_statements END SEMICOLON'
    pass

def p_for_statements(p):
    '''for_statements : for_statements for_statement
                      | for_statement'''
    pass

def p_for_statement(p):
    'for_statement : FOR ID EQUALS NUMBER SEMICOLON'
    pass

def p_error(p):
    pass

parser = yacc.yacc()

# Test input string with table, plot, and for loop syntax
input_string = "x = 10; fo i = 1:10; x = (x * 2 + 5) / 3; end;"

try:
    lexer.input(input_string)
    for tok in lexer:
        pass

    parser.parse(input_string)
    print("Valid syntax")
except SyntaxError:
    print("Invalid syntax")
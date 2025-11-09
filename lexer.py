import ply.lex as lex

# Reserved keywords
reserved = {
    'if': 'IF',
    'then': 'THEN',
    'fi': 'FI',
    'else': 'ELSE',
    'for': 'FOR',
    'in': 'IN',
    'do': 'DO',
    'done': 'DONE',
    'while': 'WHILE',
    'function': 'FUNCTION',
    'echo': 'ECHO'
}

tokens = [
    'LPAREN', 'RPAREN', 'VARIABLE', 'NUMBER', 'PLUS', 'MINUS', 'MUL', 'DIV',
     'LBRACKET', 'RBRACKET', 'LFBRACKET', 'RFBRACKET','QUOTES','DOLLAR','GT','LT','COLON','EQUAL'
] + list(reserved.values())

# Token regex definitions
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_PLUS = r'\+'
t_MINUS = r'\-'
t_MUL = r'\*'
t_DIV = r'/'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_LFBRACKET = r'\{'
t_RFBRACKET = r'\}'
t_EQUAL = r'\='
t_QUOTES = '\''
t_DOLLAR = r'\$'
t_GT = r'\>'
t_LT = r'\<'
t_COLON = r'\:'
t_ignore = ' \t'

# Rules
def t_VARIABLE(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'VARIABLE')
    return t


def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Invalid character '{t.value[0]}' at line {t.lineno}")
    t.lexer.skip(1)

# Build lexer
lexer = lex.lex()
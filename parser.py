import ply.yacc as yacc
from lexer import tokens

syntax_error = False



def p_program(p):
    '''program : statement
               | statement program'''
    pass

def p_statements(p):
    '''statements : statement
                  | statement statements'''
    pass

def p_statement_if_else(p):
    '''statement : IF LBRACKET condition RBRACKET THEN statements FI
                 | IF LBRACKET condition RBRACKET THEN statements ELSE statements FI'''
    pass

def p_statement_for(p):
    '''statement : FOR VARIABLE IN condition DO statements DONE'''
    pass

def p_statement_while(p):
    '''statement : WHILE LBRACKET condition RBRACKET DO statements DONE'''
    pass

def p_statement_function_def(p):
    '''statement : FUNCTION VARIABLE LPAREN RPAREN LFBRACKET statements RFBRACKET'''
    pass

def p_statement_assign(p):
    '''statement : VARIABLE EQUAL expression'''
    pass

def p_statement_echo(p):
    '''statement : ECHO QUOTES statements QUOTES 
                    | ECHO DOLLAR VARIABLE'''
    pass

def p_condition(p):
    '''condition : expression
    | expression operator expression'''
    pass

def p_expression(p):
    '''expression : VARIABLE
                  | NUMBER
                  | expression operator expression'''
    pass

def p_operator(p):
    '''operator : PLUS
                | MINUS
                | MUL
                | DIV
                | GT 
                | LT 
                | EQUAL'''
    pass

def p_error(p):
    global syntax_error
    syntax_error = True  
    if p:
        print(f"Syntax error at '{p.value}' (line {p.lineno}, position {p.lexpos})")
    else:
        print("Syntax error at EOF")


# Build parser
parser = yacc.yacc()

#Sabrina Margetic
#Student ID Number: 109898930
import sys, os
import re

class SemanticError(Exception):
    pass

class SyntaxError(Exception):
    pass


#list of tokens
temp = ['NEGATION','VARIABLE','LPAREN','RPAREN','NAME','REAL','INTEGER',
        'PLUS','DIVIDE','MINUS','TIMES','ID','EQUALS','COMMA','SEMICOLON','EXPONENT',
        'GREATER_EQUAL','EQUAL','NOT_EQUAL','LESS_EQUAL','LESS_THAN','GREATER_THAN',
        'HASH', 'CON','LBRACKET', 'RBRACKET', 'BOOLEAN', 'STRING']

#specific identifiers
reserved = {
    'if' : 'IF','then' : 'THEN','else' : 'ELSE','while' : 'WHILE',
    'not' : 'NOT','andalso' : 'ANDALSO','orelse' : 'ORELSE',
    'div' : 'DIV','in' : 'IN','mod': 'MOD'
}

#sum of tokens
tokens = temp + list(reserved.values())

#regular expression rules for tokens
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_PLUS    = r'\+'
t_DIVIDE  = r'/'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_EXPONENT = r'\*\*'
t_CON = r'::'
t_LESS_THAN = r'<'
t_LESS_EQUAL = r'<='
t_EQUAL = r'=='
t_EQUALS = r'='
t_NOT_EQUAL = r'<>'
t_GREATER_THAN = r'>'
t_GREATER_EQUAL = r'>='
t_HASH = r'\#'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'

t_MOD = r'(mod)'
t_DIV = r'(div)'
t_COMMA = r','
t_IN = r'(in)'
t_NOT = r'(not)'
t_ANDALSO = r'(andalso)'
t_ORELSE = r'(orelse)'
#NEED TO FIX
# t_NAME    = r'[a-zA-Z_][a-zA-Z0-9_]*'


INTEGER = r'[0-9]([0-9])*'
BOOLEAN = r'(False)|(True)'
REAL = r'(-?[0-9]*\.[0-9]([0-9])*)|(-?[0-9][0-9]*\.[0-9][0-9]*)'
STRING = r'([\'][a-zA-Z0-9\[\]\*\+\?\|\.\\/\{\}=_;:><@%!&\$\^\t\- ]*[\'])|([\"][a-zA-Z0-9\[\]\*\+\?\|\.\\/\{\}=_;:><@%!&\$\^\t\- ]*[\"])'


#the types accepted by our language
def t_BOOLEAN(t):
        r'(False)|(True)'
        return t

def t_STRING(t):
        r'([\'][a-zA-Z0-9\[\]\*\+\?\|\.\\/\{\}=_;:><@%!&\$\^\t\- ]*[\'])|([\"][a-zA-Z0-9\[\]\*\+\?\|\.\\/\{\}=_;:><@%!&\$\^\t-\- ]*[\"])'
        return t

def t_REAL(t):
        r'(-?[0-9]*\.[0-9]([0-9])*)|(-?[0-9][0-9]*\.[0-9][0-9]*)'
        t.value = float(t.value)
        return t

def t_INTEGER(t):
        r'(-?[1-9]([0-9])*)|([0-9]([0-9])*)'
        t.value = int(t.value)    
        return t


t_ignore = ' \t'


def t_newline(t):
        r'\n+'

def t_error(t):
        raise SyntaxError()
def t_comment(t):
    r'//.*'
    pass



import ply.lex as lex
lexer = lex.lex(debug=True)



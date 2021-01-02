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
        'HASH', 'CON','LBRACKET', 'RBRACKET', 'BOOLEAN', 'STRING', 'PRINT', 'CURLYL', 'CURLYR'
        ]


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
# t_MINUS   = r'-'
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
t_CURLYL = r'\{'
t_CURLYR = r'\}'
t_SEMICOLON = r';'


INTEGER = r'[0-9]([0-9])*'
BOOLEAN = r'(False)|(True)'
REAL = r'(-?[0-9]*\.[0-9]([0-9])*)|(-?[0-9][0-9]*\.[0-9][0-9]*)|(^-*\d*e*E*-*\d*\.-*\d*e*E*-*\d*$)'
STRING = r'([\'][a-zA-Z0-9\[\]\*\+\?\|\.\\/\{\}=_;:><@%!&\$\^\t\- ]*[\'])|([\"][a-zA-Z0-9\[\]\*\+\?\|\.\\/\{\}=_;:><@%!&\$\^\t\- ]*[\"])'

def t_MINUS(t):
        r'-'
        return t

def t_ORELSE(t):
        r'(orelse)'
        return t

def t_ANDALSO(t):
        r'(andalso)'
        return t

def t_NOT(t):
        r'(not)'
        return t

def t_COMMA(t):
        r','
        return t

def t_MOD(t):
        r'(mod)'
        return t

def t_DIV(t):
        r'(div)'
        return t

def t_IN(t):
        r'(in)' #MUST FIX
        return t
#the types accepted by our language
def t_BOOLEAN(t):
        r'(False)|(True)'
        return t

#DO WE DO THE REGULAR EXPRESSIONS LIKE THIS??
def t_WHILE(t):
        r'while'
        return t

def t_IF(t):
        r'if'
        return t

def t_PRINT(t):
        r'print'
        return t

def t_ELSE(t):
        r'else'
        return t

def t_NAME(t):
        r'[a-zA-Z_][a-zA-Z0-9_]*'
        return t

def t_STRING(t):
        r'([\'][a-zA-Z0-9\[\]\*\+\?\|\.\\/\{\}=_;:><@%!&\$\^\t\- ]*[\'])|([\"][a-zA-Z0-9\[\]\*\+\?\|\.\\/\{\}=_;:><@%!&\$\^\t\- ]*[\"])'
        return t

def t_REAL(t):
        r'([0-9]*\.[0-9]*e-?[0-9]*)|([0-9]*\.[0-9]*E-?[0-9]*)|(-?[0-9]*\.[0-9]([0-9])*)|(-?[0-9][0-9]*\.[0-9]*)'
        #(^-*\d*e*E*-*\d*\.-*\d*e*E*-*\d*$)'
        t.value = float(t.value)
        return t

def t_INTEGER(t):
        r'(-?[1-9]([0-9])*)|([0-9]([0-9])*)'
        t.value = int(t.value)    
        return t



def t_newline(t):
        # r'\n+'
        r'\n+'


# t_ignore = r'[ \t\n]'
t_ignore = ' \t'
# t_ignore_newline = '\n'

def t_error(t):
        raise SyntaxError()
def t_comment(t):
    r'//.*'
    pass



import ply.lex as lex
lexer = lex.lex(debug=True) #REMEMBER TO CHANGE

# f = open("test.txt", "r")
# for line in f:
#         lex.input(line)
# while True:
#      tok = lexer.token()
#      if not tok: 
#          break      # No more input
#      print(tok)
 


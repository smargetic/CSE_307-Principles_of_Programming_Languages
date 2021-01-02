#Sabrina Margetic
#Student ID Number: 109898930

import sbml_lexer
import sbml_nodes
tokens = sbml_lexer.tokens


precedence = (
        ('left','PLUS','MINUS'),('left', 'GREATER_THAN'), ('left','LESS_THAN'),
        ('left', 'LESS_EQUAL'), ('left', 'GREATER_EQUAL'), ('left', 'EQUAL'),
        ('left', 'EQUALS'),('left','TIMES'), ('left','DIVIDE'),('left', 'HASH'),
        ('right','EXPONENT'), ('right', 'CON'), ('left', 'MOD'), ('left', 'LBRACKET', 'RBRACKET')
        )

names = {}

#function to append stuff
def appendStuff(x,y):
    x.value.append(y)

#assign expressions based on type
def p_expression_integer(p):
    'expression : INTEGER'
    p[0] = sbml_nodes.Number(p[1])

def p_expression_real(p):
    'expression : REAL'
    p[0] = sbml_nodes.Number(p[1])

def p_expression_boolean(p):
    'expression : BOOLEAN'
    p[0] = sbml_nodes.Boolean(p[1])

def p_expression_string(p):
    'expression : STRING'
    p[0] = sbml_nodes.String(p[1])

def p_expression_list(p):
    'expression : list'
    p[0] = p[1]


def p_expression_tuple(p):
    'expression : tuple'
    p[0] = p[1]

# #assign acutal values
# def p_statement_assign(p):
#     'statement : NAME EQUALS expression'
#     names[p[1]] = p[3]

#Binomial operators
def p_expression_binop(p): #Not sure if should specify if interger or something for plus
    '''expression : expression PLUS expression
            | expression MINUS expression
            | expression TIMES expression
            | expression DIVIDE expression
            | expression EXPONENT expression
            | expression DIV expression
            | expression MOD expression
            '''

    p[0] = sbml_nodes.BinomialOp(p[1], p[2], p[3])

#boolean operators
def p_expression_boolop(p):
    '''expression : BOOLEAN ORELSE BOOLEAN
        | BOOLEAN ANDALSO BOOLEAN
        | NOT BOOLEAN '''
    if (len(p)==3):
        p[0] = sbml_nodes.Negation(p[2])
    else:
        p[0] = sbml_nodes.booleanConjDisj(p[1],p[2],p[3])

#comparison operators
def p_expression_Comp(p):
    '''expression : expression LESS_THAN expression
    | expression GREATER_THAN expression
    | expression LESS_EQUAL expression
    | expression GREATER_EQUAL expression
    | expression EQUAL expression
    | expression NOT_EQUAL expression'''
    p[0] = sbml_nodes.ComparisonOp(p[1],p[2],p[3])


#list stuff
def p_list(p):
    'list : LBRACKET centerList RBRACKET'
    p[0]= p[2]

def p_centerList_comma(p):
    'centerList : centerList COMMA expression'
    # p[1].value.append(p[3])
    appendStuff(p[1],p[3])
    p[0] = p[1]

def p_centerList(p):
    'centerList : expression'
    p[0] = sbml_nodes.listNode(p[1])

def p_expression_InList(p):
    'expression : expression IN list'
    p[0] = sbml_nodes.inOperator(p[1], p[3])

def p_expression_ConjList(p):
    'expression : list CON list'
    p[0] = sbml_nodes.conjOperator(p[1], p[3])

def p_list_empty(p):
    'list : LBRACKET RBRACKET'
    p[0] = sbml_nodes.listNode(None)

def p_list_index(p):
    'expression : expression LBRACKET expression RBRACKET'
    p[0] = sbml_nodes.listIndex(p[1], p[3])

#parenthesis
def p_paren(p):
    'expression : LPAREN expression RPAREN'
    p[0] = sbml_nodes.parenNode(p[2])

#tuple stuff
def p_tuple(p):
    'tuple : LPAREN centerTuple RPAREN'
    p[0] = p[2]

def p_tuple_1(p):
    'tuple : LPAREN centerTuple COMMA RPAREN'
    p[0] = p[2]

def p_centerTuple_comma(p):
    'centerTuple : centerTuple COMMA expression'
    appendStuff(p[1],p[3])
    p[0] = p[1]

def p_centerTuple(p):
   'centerTuple : expression'
   p[0] = sbml_nodes.tupleNode(p[1])

def p_expression_InTuple(p):
    'expression : expression IN tuple'
    p[0] = sbml_nodes.inOperator(p[1], p[3])

def p_expression_ConjTuple(p):
    'expression : tuple CON tuple'
    p[0] = sbml_nodes.conjOperatorTuple(p[1], p[3])

def p_expression_tupleIndex(p):
    'expression : HASH expression tuple'
    p[0] = sbml_nodes.tupleIndex(p[2], p[3])

#error
def p_error(p):
    raise sbml_lexer.SyntaxError(Exception)



import ply.yacc as yacc
parser = yacc.yacc(debug = True)

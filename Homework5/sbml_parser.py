#Sabrina Margetic
#Student ID Number: 109898930

import sbml_lexer
import sbml_nodes
tokens = sbml_lexer.tokens


precedence = (
        ('left', 'EQUALS'),
        ('right', 'CON'), 

        ('left', 'NOT', 'ANDALSO', 'ORELSE'),
        ('left', 'IN'),
        
        ('left', 'GREATER_THAN'), ('left','LESS_THAN'), ('left', 'LESS_EQUAL'), ('left', 'GREATER_EQUAL'), 
        ('left', 'EQUAL'), ('left', 'NOT_EQUAL'),

        ('left','PLUS','MINUS'),
        ('left', 'MOD', 'DIV'),
        ('left','TIMES', 'DIVIDE'),
        ('right','EXPONENT'),
        ('left', 'HASH', 'LBRACKET', 'RBRACKET')

        )


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
    '''expression : expression ORELSE expression
        | expression ANDALSO expression
        | NOT expression '''
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
    appendStuff(p[1],p[3])
    p[0] = p[1]

def p_centerList(p):
    'centerList : expression'
    p[0] = sbml_nodes.listNode(p[1])

def p_expression_InList(p):
    'expression : expression IN expression'
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


def p_expression_ConjTuple(p):
    'expression : tuple CON tuple'
    p[0] = sbml_nodes.conjOperatorTuple(p[1], p[3])

def p_expression_tupleIndex(p):
    'expression : HASH expression tuple'
    p[0] = sbml_nodes.tupleIndex(p[2], p[3])

#error
def p_expression_ConSingleList(p):
    'expression : expression CON list'
    p[0] = sbml_nodes.conjOperator(p[1], p[3])

def p_expression_ConSingleTuble(p):
    'expression : expression CON tuple'
    p[0] = sbml_nodes.conjOperatorTuple(p[1], p[3])

    
def p_expression_statements(p):
    '''expression : bigBlock'''
    p[0] = p[1]


def p_bigBlockInRec(p):
    '''bigBlockIn : bigBlockIn statement
                    | bigBlockIn block'''
    if(isinstance(p[1], list)):
        p[0] = p[1] + [p[2]]
    else:
        p[0] = [p[2]]

#migh need to fix
def p_bigBlockIn(p):
    '''bigBlockIn : block'''
    p[0] = [p[1]]


# def p_statementBlock(p):
#     'statement : block'
#     print("in block")
#     p[0] = p[1]

def p_block(p):
    '''block : CURLYL blockIn CURLYR
            | CURLYL CURLYR
            | blockIn'''
    if(len(p)==3):
        p[0]= sbml_nodes.blockNode([])
    elif(len(p)==4):
        p[0]= sbml_nodes.blockNode(p[2])
    else:
        p[0]= sbml_nodes.blockNode(p[1])

def p_bigBlock(p):
    '''bigBlock : CURLYL bigBlockIn CURLYR
                | CURLYL CURLYR'''
    if len(p)==4:
        p[0]= sbml_nodes.blockNode(p[2])
    else:
        p[0] = sbml_nodes.blockNode([])

def p_expression_name(p):
    'expression : NAME'
    p[0] = p[1]
#STATEMENT STUFF

def p_statement_statement(p):
    '''blockIn : blockIn statement'''
    if(isinstance(p[1], list)):
        p[0] = p[1] + [p[2]]
    else:
        p[0] = [p[2]]
    
def p_statement2(p):
    '''blockIn : statement '''
    p[0] = [p[1]]
#ADD ANOTHER GRAMMER FOR STATEMENT --> like block

def p_expression_equals(p):
    '''statement : NAME EQUALS expression SEMICOLON'''
    p[0] = sbml_nodes.nameNode(p[1], p[3])


def p_expression_print(p):
    '''statement : PRINT LPAREN expression RPAREN SEMICOLON'''
    p[0] = sbml_nodes.printNode(p[3])


def p_statement_while(p):
    '''statement : WHILE LPAREN expression RPAREN block'''
    p[0] = sbml_nodes.whileNode(p[3], p[5])

def p_statement_if_else(p):
    '''statement : IF LPAREN expression RPAREN block ELSE block'''
    p[0] = sbml_nodes.ifElseNode(p[3], p[5], p[7])       


def p_statement_if(p):
    '''statement : IF LPAREN expression RPAREN block'''
    p[0] = sbml_nodes.ifNode(p[3], p[5])



#new for functions
def p_expression_entire(p):
    '''expression : entire'''

    p[0] = sbml_nodes.blockNode(p[1])

#need to hold functions, and then main block
def p_functions_bigBlock(p):
    '''entire : funIn bigBlock'''
    p[0] = [p[2]]

def p_funIn(p):
    '''funIn : function
            | function funIn '''
      
    

def p_expression_fun(p):
    '''function : FUN NAME LPAREN centerExp RPAREN EQUALS block expression SEMICOLON
            | FUN NAME LPAREN RPAREN EQUALS block expression SEMICOLON'''
    if(len(p)==10):
        sbml_nodes.funNode(p[2], p[4], p[7], p[8])
    else:
        sbml_nodes.funNode(p[2], [], p[6], p[7])


def p_statement_expSemi(p):
    '''statement : expression SEMICOLON'''
    p[0] = p[1]

def p_expression_funcEval(p):
    'expression : funcEval'
    p[0] = p[1]

def p_expression_funeval(p):
    '''funcEval : NAME LPAREN centerExp RPAREN
                | NAME LPAREN RPAREN'''
    if(len(p)==5):
        p[0] = sbml_nodes.funCalledNode(p[1], p[3])
    else:
        p[0] = sbml_nodes.funCalledNode(p[1], [])

def p_centerexp_expression(p):
    '''centerExp : expression '''
    p[0]= [p[1]]
    

def p_centerexp_comma(p):
    '''centerExp : centerExp COMMA expression '''
    p[1].append(p[3])
    p[0] = p[1]


def p_error(p):
    raise sbml_lexer.SyntaxError(Exception)



import ply.yacc as yacc
parser = yacc.yacc(debug = False)



# def p_expression_funceval(p):
#     'expression : funcEval'
#     p[0] = p[1]
# def p_statement_expression(p):
#     '''expression : statement'''
#     p[0] = p[1]

#fun in
    # if(len(p)!=2):
    #     if(isinstance(p[1], list)):
    #         p[0] = p[1] + [p[2]]
    #     else:
    #         p[0] = [p[2]]
    # else:
    #     p[0] =[p[1]]  
        # if(isinstance(p[1],list)):
    #     p[0] = p[1] + [p[2]]
    # else:
    #     p[0] = [p[2]]

    # if(len(p)!=2):
    #     if(isinstance(p[1], list)):
    #         p[0] = p[1] + [p[2]]
    #     else:
    #         p[0] = [p[2]]
    # else:
    #     p[0] =[p[1]]
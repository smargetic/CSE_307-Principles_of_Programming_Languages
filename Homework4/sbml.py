#Sabrina Margetic
#Student ID Number: 109898930

import sys, getopt
import sbml_parser
import sbml_lexer
import re

parser = sbml_parser.parser
lex = sbml_lexer.lexer



def main():
    #UNCOMMENT LATER
    opts, arg = getopt.getopt(sys.argv[1:],'x', ['condition=', 'output-file=', 'testing'])
    f = open(arg[0], "r")

    # f = open("test.txt", "r")
    tempStr = ""
    for line in f:
        tempStr = tempStr + line
    
    lex.input(tempStr)
    # while True:
    #     tok = lex.token()
    #     if not tok: 
    #         break      # No more input
    #     print(tok)

    try:
        result = parser.parse(tempStr)
        result.eval()
    except sbml_lexer.SyntaxError:
        print("SYNTAX ERROR")
    except sbml_lexer.SemanticError:
        print("SEMANTIC ERROR")


#
main()
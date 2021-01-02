#Sabrina Margetic
#Student ID Number: 109898930

import sys, getopt
import sbml_parser
import sbml_lexer

parser = sbml_parser.parser
lex = sbml_lexer.lexer


def main():
    #UNCOMMENT LATER
    # opts, arg = getopt.getopt(sys.argv[1:],'x', ['condition=', 'output-file=', 'testing'])
    # f = open(arg[0], "r")
    f = open("test.txt", "r")
    for line in f:
        lex.input(line)
        try:
            result = parser.parse(line)
            print(result.eval())
        except sbml_lexer.SyntaxError:
            print("SYNTAX ERROR")
        except sbml_lexer.SemanticError:
            print("SEMANTIC ERROR")


#
main()
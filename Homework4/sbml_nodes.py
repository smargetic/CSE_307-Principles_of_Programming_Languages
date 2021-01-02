#Sabrina Margetic
#Student ID Number: 109898930

import sbml_lexer
import inspect

names = {}
#make sure that they are same
def typeChecking(left, right):
    if(type(left)is type(right)):
        return True
    elif(isinstance(left,int) and isinstance(right,float)):
        return True
    elif(isinstance(left,float) and isinstance(right,int)):
        return True
    return False

def numberCheck(left, right):
    if (isinstance(left, int) or isinstance(left, float)):
        if (isinstance(right, int) or isinstance(right,float)):
            return True
    return False

def stringCheck(left, right):
    if (isinstance(left, str) and isinstance(left, str)):
        return True
    return False

def primTypeCheck(item):
    if (isinstance(item, str)):
        return True
    if (isinstance(item, int)):
        return True
    if (isinstance(item, bool)):
        return True
    if (isinstance(item, float)):
        return True
    return False

def primTypeCheck2(item):
    if (type(item) == str):
        return True
    if (type(item)==int):
        return True
    if (type(item)== bool):
        return True
    if (type(item)==float):
        return True
    return False

def moreTypeCheck(item):
    if(isinstance(item, tuple)):
        return True
    if(isinstance(item, list)):
        return True
    return False

#data types
class Number:
    def __init__(self, value):
        super().__init__()
        if(isinstance(value,int)or isinstance(value,float)):
            self.value = value
        else:
            raise sbml_lexer.SemanticError()

    def eval(self):
        return self.value


class Boolean:
    def __init__(self, value):
        super().__init__()
        #type checking
        if(value=="True"):
            self.value = True
        elif(value =="False"):
            self.value = False
        else:
            raise sbml_lexer.SemanticError()
    def eval(self):
        return self.value

class String:
    def __init__(self, value):
        super().__init__()
        #must make sure is string
        # self.value = value
        self.value = str(value)[1:-1]

    def eval(self):
        return self.value



#DOUBLE CHECK
class listNode:
    def __init__(self, value):
        if(value!=None):
            self.value = [value]
        else:
            self.value = [None]
    
    def eval(self):
        tempList = []
        if(self.value!=[None]):
            for item in self.value:
                tempList.append(item.eval())
            return tempList
        else:
            return []



class tupleNode:
    def __init__(self, value):
        if(value!=None):
            self.value = [value]
        else:
            self.value = [None]

    
    def eval(self):
        tempList = []
        count = 0
        for item in self.value:
            count = count + 1
        if(self.value!=[None]):
            if(count>1):
                for item in self.value:
                    tempList.append(item.eval())

                
                tupleTemp = tuple(tempList)
                return tupleTemp
            elif(count ==1):
                for item in self.value:
                    return tuple([item.eval()])
        else:
            return ()

    
class listIndex:
    def __init__(self, left, right):
        super().__init__()
        self.left = left
        self.right = right
    
    def eval(self):
        tempL = self.left
        tempR = self.right
        #if either is a name
        if (tempL in names):
            if (tempR in names):

                return names[tempL][names[tempR]]
            return names[tempL][tempR.eval()]
        
        tempL = self.left.eval()
        tempR = self.right.eval()

        #error checking
        if(isinstance(tempL,str)or isinstance(tempL, list)):
            if(type(tempR)!=int):
                raise sbml_lexer.SemanticError()
        else:
            raise sbml_lexer.SemanticError()

        count = 0
        temp = []
        if (isinstance(tempL, str)):
            temp = list(tempL)
        else:
            temp = tempL
        
        for item in temp:
            count = count + 1
        
        if ((count-1)<tempR):
            raise sbml_lexer.SemanticError()

        return temp[tempR]

class tupleIndex: #CHANGE EVAL
    def __init__(self, left, right):
        super().__init__()
        self.left = left
        self.right = right

    def eval(self):
        tempLeft = self.left.eval()
        tempRight = self.right.eval()
        
        if(not isinstance(tempLeft,int)):
            raise sbml_lexer.SyntaxError()
        if(not isinstance(tempRight,tuple)):
            raise sbml_lexer.SyntaxError()
        
        count = 0
        for item in tempRight:
            count = count + 1
        if ((count)<tempLeft):
            raise sbml_lexer.SemanticError()

        count2 = 1
        for item in tempRight:
            if count2==tempLeft:
                return item
            count2 = count2 + 1

#OPERATORS
class Negation:
    def __init__(self, value):
        self.value = value

    def eval(self):
        temp = self.value
        if(temp in names):
            temp = names[temp]
        else:
            temp = self.value.eval()
        if ((temp!=True) and (temp!=False)):
            raise sbml_lexer.SemanticError()
        return not temp

class booleanConjDisj:
    def __init__(self, left, op, right):
        self.left = left
        self.right = right
        self.op = op

    def eval(self):
        tempL = self.left
        if (tempL in names):
            tempL = names[tempL]
        else:
            tempL = self.left.eval() #NOT SURE IF TOOK OUT EVALS FOR SOME REASON BEFORE
        
        tempR= self.right
        if (tempR in names):
            tempR = names[tempR]
        else:
            tempR = self.right.eval() #NEED TO cOME BACK TO SEE WHAT TO DO IF GIVEN false instead of False

        if(typeChecking(tempL, tempR)==False):

            raise sbml_lexer.SemanticError()
        if((tempL!=True) and (tempL!=False)):

            raise sbml_lexer.SemanticError()
        if((tempR!=True) and (tempR!=False)):
            raise sbml_lexer.SemanticError()

        if(self.op =='andalso'):
            return tempL and tempR
        elif(self.op == 'orelse'):
            return tempL or tempR

        
class BinomialOp:
    def __init__(self, left, oper, right):
        super().__init__()
        self.left = left
        self.right = right
        self.oper = oper
        self.type = "binOp"
    def eval(self):
        tempLeft = self.left
        tempRight = self.right

        if(self.left in names):
            tempLeft = names[self.left]
        elif (primTypeCheck(self.left)==False): #CHECK IF PRIM TYPE
            tempLeft = self.left.eval()
        if(self.right in names):
            tempRight = names[self.right]
        elif (primTypeCheck(self.right)==False): #CHECK IF PRIM TYPE
            tempRight = self.right.eval()

        if((self.oper =='-')and (numberCheck(tempLeft,tempRight)==False)):
            raise sbml_lexer.SemanticError()
        if (self.oper== '-'):
            return (tempLeft-tempRight)
            # return (self.left-self.right)
        elif((self.oper=='+') and (typeChecking(tempLeft,tempRight)==False)):
            raise sbml_lexer.SemanticError()
        elif((self.oper == '+') and (not (isinstance(tempLeft, str) or numberCheck(tempLeft,tempRight) or isinstance(tempLeft, list)))):
            raise sbml_lexer.SemanticError()
        elif (self.oper=='+'):
            return (tempLeft+tempRight)
        elif((self.oper == '*') and (numberCheck(tempLeft,tempRight)==False)):
            raise sbml_lexer.SemanticError()
        elif (self.oper=='*'):
            return (tempLeft*tempRight)
        elif((self.oper == '/') and (numberCheck(tempLeft,tempRight)==False)):
            raise sbml_lexer.SemanticError()
        elif (self.oper=='/'):
            if(tempRight==0):
                raise sbml_lexer.SemanticError()
            return float(tempLeft)/float(tempRight)
        elif((self.oper == '**') and (numberCheck(tempLeft,tempRight)==False)):
            raise sbml_lexer.SemanticError()
        elif (self.oper=='**'):
            if(numberCheck(tempLeft, tempRight)==False):
                raise sbml_lexer.SemanticError()  
            return (tempLeft**tempRight)
        elif((self.oper=='div') and (not (isinstance(tempLeft, int) and isinstance(tempRight, int)))):
            raise sbml_lexer.SemanticError()
        elif (self.oper=='div'):
            return int(tempLeft/tempRight) #DOUBLE CHECK HTIS
        elif((self.oper=='mod') and (not (isinstance(tempLeft, int) and isinstance(tempRight, int)))):
            raise sbml_lexer.SemanticError()
        elif(self.oper=='mod'):
            return (tempLeft)%(tempRight)


class inOperator:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def eval(self):
        tempRight = self.right
        if(tempRight in names):
            tempRight = names[tempRight]
        elif(type(tempRight)!= str):
            tempRight = self.right.eval()
        
        tempLeft = self.left.eval()
        if((not isinstance(tempRight, list)) and (not isinstance(tempRight,tuple)) and (not isinstance(tempRight, str))):
            raise sbml_lexer.SemanticError()

        return tempLeft in tempRight #double check
    

class conjOperator:
    def __init__(self, left, right): #MUST FIX
        self.left = left
        self.right = right

    def eval(self):
        tempLeft = self.left
        tempRight = self.right
        if(typeChecking(tempLeft, tempRight)==True):
            if(not isinstance(tempLeft.eval())):
                raise sbml_lexer.SemanticError()
            else:
                tempLeft = self.left.eval()
                tempRight = self.right.eval()
        else:
            if((primTypeCheck(self.left.eval())==True) and (isinstance(self.right.eval(), list))) :
                tempLeft = self.left.eval()
                tempRight = self.right.eval()
            else:
                raise sbml_lexer.SemanticError()
        
        tempList = []
        if (isinstance(tempLeft, list)):
            for i in tempLeft:
                tempList.append(i)
        else:
            tempList.append(tempLeft)
        for i in tempRight:
            tempList.append(i)
        return tempList

class conjOperatorTuple:
    def __init__(self, left, right):
        if(typeChecking(left,right)==True): #MUST FIX TO NOT HAVE EVAL
            if(isinstance(left.eval(), tuple)):
                super().__init__()
                self.left = left.eval()
                self.right = right.eval()
            else:
                raise sbml_lexer.SemanticError()
        else: 
            raise sbml_lexer.SemanticError()
    def eval(self):
        tempList = []
        for i in self.left:
            tempList.append(i)
        for i in self.right:
            tempList.append(i)

        tupleFinal = tuple(tempList)
        return tupleFinal

class parenNode:
    def __init__(self, value):
        super().__init__()
        self.value = value
    def eval(self):
        return (self.value.eval())
        # return "(" + str(self.value) + ")"


class ComparisonOp:
    def __init__(self, left, op, right):
        super().__init__()
        self.left = left
        self.right = right
        self.op = op


    def eval(self):
        tempLeft = self.left
        tempRight = self.right


        if(self.left in names):
            tempLeft = names[self.left]
        elif ((not isinstance(self.left, int)) and (not isinstance(self.left,float))):
            tempLeft = self.left.eval()

        if(self.right in names):
            tempRight = names[self.right]
        elif ((not isinstance(self.right, int)) and (not isinstance(self.right,float))): #DOUBLE CHECK THAT THESE ARE THE ONLY ONES THAT CAN BE PASSE
            tempRight = self.right.eval()
        if (self.op=='<'):
            return (tempLeft<tempRight)
        elif(self.op=='>'):
            return (tempLeft>tempRight)
        elif(self.op=='<='):
            return (tempLeft<=tempRight)
        elif(self.op=='>='):
            return (tempLeft>=tempRight)
        elif(self.op=='=='):
            return (tempLeft==tempRight)
        elif(self.op=='<>'):
            return not(tempLeft==tempRight)


#NEW STUFF
class nameNode:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def eval(self):
        global names
    
        if(self.right in names):
            self.right = names[self.right]

        if(type(self.right)==str):
            if((self.right[0] != "\"") and (self.right[0]!= "'")):
                raise sbml_lexer.SemanticError()

        if(type(self.right)!=int):
            if (self.right in names):
                names[self.left] = names[self.right]
            else:
                names[self.left] = self.right.eval()
        else:
            names[self.left] = self.right


class printNode:
    def __init__(self, value):
        self.value = value

    def eval(self):
        val = self.value
        if(not isinstance(val, str)): 
            val = self.value.eval()

        if (val in names):
            print(names[val])
        else:
            print(val)

class ifNode:
    def __init__(self,value, block):
        self.value = value
        self.block = block

    def eval(self):
        val = self.value
        if(val in names):
            val = names[val]
        if((type(val)==str) or (type(val)==int) or (type(val)==float) or (type(val)==list) or (type(val)==tuple)):
            raise sbml_lexer.SemanticError()
        if(type(val)!= bool):
            val = self.value.eval()

        if((val != True) and (val!= False) ):
            raise sbml_lexer.SemanticError()
        if(val==False):
            return
        else:
            self.block.eval()
            return


class ifElseNode:
    def __init__(self,value, blockIf, blockElse):
        self.value = value
        self.blockIf = blockIf
        self.blockElse = blockElse

    def eval(self):
        val = self.value
        if(val in names):
            val = names[val]
        else:
            val = self.value.eval()

        if((val != True) and (val!= False) ):
            raise sbml_lexer.SemanticError()
        if(val==False):
            self.blockElse.eval()
        else:
            self.blockIf.eval()


class whileNode:
    def __init__(self, value, block):
        self.value = value
        self.block = block

    def eval(self):
        if(self.value in names):
            while(names[self.value]):
                self.block.eval()
        else:
            while(self.value.eval()):
                self.block.eval()


class blockNode:
    def __init__(self, value):
        self.value = value
    def eval(self):
        if(self.value == []):
            return

        for items in self.value:
            items.eval()


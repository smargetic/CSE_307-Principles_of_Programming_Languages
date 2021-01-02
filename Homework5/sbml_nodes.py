#Sabrina Margetic
#Student ID Number: 109898930

import sbml_lexer
import inspect
import copy
# from builtins import str

names = {}
tempStack = []
stack = []
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
        #if either is a name in the stack
        if(len(stack)>0):
            if(type(tempL)!=list):
                if(tempL in stack[len(stack)-1]["names"]):
                    if(type(tempR)!=list):
                        if(tempR in stack[len(stack)-1]["names"]):
                            return stack[len(stack)-1]["names"][tempL][stack[len(stack)-1]["names"][tempR]]
                        return stack[len(stack)-1]["names"][tempL][tempR.eval()]
                    else:
                        if(tempR in stack[len(stack)-1]["names"].values()):
                            return stack[len(stack)-1]["names"][tempL][stack[len(stack)-1]["names"][tempR]]
                        return stack[len(stack)-1]["names"][tempL][tempR.eval()]                     
            else:
                if(tempL in stack[len(stack)-1]["names"].values()):
                    if(type(tempR)!=list):
                        if(tempR in stack[len(stack)-1]["names"]):
                            return stack[len(stack)-1]["names"][tempL][stack[len(stack)-1]["names"][tempR]]
                        return stack[len(stack)-1]["names"][tempL][tempR.eval()]
                    else:
                        if(tempR in stack[len(stack)-1]["names"].values()):
                            return stack[len(stack)-1]["names"][tempL][stack[len(stack)-1]["names"][tempR]]
                        return stack[len(stack)-1]["names"][tempL][tempR.eval()]  
        #if either is a name
        if(type(tempL)!=list):
            if (tempL in names):
                if(type(tempR)!=list):
                    if (tempR in names):

                        return names[tempL][names[tempR]]
                    return names[tempL][tempR.eval()]
                else:
                    if (tempR in names.values()):

                        return names[tempL][names[tempR]]
                    return names[tempL][tempR.eval()]
        else:
            if (tempL in names.values()):
                if(type(tempR)!=list):
                    if (tempR in names):

                        return names[tempL][names[tempR]]
                    return names[tempL][tempR.eval()]
                else:
                    if (tempR in names.values()):

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

        tempRight = self.right

        #if in stack
        if(len(stack)>0):
            if(type(tempRight)!=list):
                if(tempRight in stack[len(stack)-1]["names"]):
                    tempRight = stack[len(stack)-1]["names"][tempRight]
            else:
                if(tempRight in stack[len(stack)-1]["names"].values()):
                    tempRight = stack[len(stack)-1]["names"][tempRight]              
        #if in names
        if(type(tempRight)!=list):
            if(tempRight in names):
                tempRight = names[tempRight]
            else:
                tempRight = self.right.eval()
        else:
            if(tempRight in names.values()):
                tempRight = names[tempRight]
            else:
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
        if(len(stack)>0):
            if(type(temp)!=list):
                if(temp in stack[len(stack)-1]["names"]):
                    temp = stack[len(stack)-1]["names"][temp]
            else:
                if(temp in stack[len(stack)-1]["names"].values()):
                    temp = stack[len(stack)-1]["names"][temp]
        if(type(temp)!=list):
            if(temp in names):
                temp = names[temp]
            else:
                temp = self.value.eval()
        else:
            if(temp in names.values()):
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
        #if there is something in the stack
        if(len(stack)>0):
            if(type(tempL)!=list):
                if(tempL in stack[len(stack)-1]["names"]):
                    tempL = stack[len(stack)-1]["names"][tempL]
            else:
                if(tempL in stack[len(stack)-1]["names"].values()):
                    tempL = stack[len(stack)-1]["names"][tempL]
        
        if(type(tempL) !=list):
            if (tempL in names):
                tempL = names[tempL]
            else:
                tempL = self.left.eval() #NOT SURE IF TOOK OUT EVALS FOR SOME REASON BEFORE
        else:
            if (tempL in names.values()):
                tempL = names[tempL]
            else:
                tempL = self.left.eval() 
        
        tempR= self.right
        if(len(stack)>0):
            if(type(tempR)!=list):
                if(tempR in stack[len(stack)-1]["names"]):
                    tempR = stack[len(stack)-1]["names"][tempR]
            else:
                if(tempR in stack[len(stack)-1]["names"].values()):
                    tempR = stack[len(stack)-1]["names"][tempR]                
        
        if(type(tempR)!=list):
            if (tempR in names):
                tempR = names[tempR]
            else:
                tempR = self.right.eval() #NEED TO cOME BACK TO SEE WHAT TO DO IF GIVEN false instead of False
        else:
            if (tempR in names.values()):
                tempR = names[tempR]
            else:
                tempR = self.right.eval()

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

        #if there is something present in the stack
        if(len(stack)>0):
            if(type(self.left)!=list):
                if(self.left in stack[len(stack)-1]["names"]):
                    tempLeft = stack[len(stack)-1]["names"][self.left]
            else:
                if(self.left in stack[len(stack)-1]["names"].values()):
                    tempLeft = stack[len(stack)-1]["names"][self.left]
            
            if(type(self.right)!=list):
                if(self.right in stack[len(stack)-1]["names"]):
                    tempRight = stack[len(stack)-1]["names"][self.right]
            else:
                if(self.right in stack[len(stack)-1]["names"].values()):
                    tempRight = stack[len(stack)-1]["names"][self.right]

        if(type(self.left)!=list):
            if(self.left in names):
                tempLeft = names[self.left]
            elif (primTypeCheck(self.left)==False): #CHECK IF PRIM TYPE
                while(primTypeCheck(tempLeft)==False):
                    tempLeft = tempLeft.eval()
                tempLeft = self.left.eval()
        else:
            if(self.left in names.values()):
                tempLeft = names[self.left]
            elif (primTypeCheck(self.left)==False): #CHECK IF PRIM TYPE
                while(primTypeCheck(tempLeft)==False):
                    tempLeft = tempLeft.eval()
                tempLeft = self.left.eval()
        
        if(type(self.right)!=list):
            if(self.right in names):
                tempRight = names[self.right]
            elif (primTypeCheck(self.right)==False): #CHECK IF PRIM TYPE
                while(primTypeCheck(tempRight)==False):
                    tempRight = tempRight.eval()
        else:
            if(self.right in names.values()):
                tempRight = names[self.right]
            elif (primTypeCheck(self.right)==False): #CHECK IF PRIM TYPE
                while(primTypeCheck(tempRight)==False):
                    tempRight = tempRight.eval()            


        if((self.oper =='-')and (numberCheck(tempLeft,tempRight)==False)):
            raise sbml_lexer.SemanticError()
        if (self.oper== '-'):
            return (tempLeft-tempRight)
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
        #if in stack
        if(len(stack)>0):
            if(type(tempRight)!=list):
                if(tempRight in stack[len(stack)-1]["names"]):
                    tempRight = stack[len(stack)-1]["names"][tempRight]
            else:
                if(tempRight in stack[len(stack)-1]["names"].values()):
                    tempRight = stack[len(stack)-1]["names"][tempRight]
        if(type(tempRight)!=list):       
            if(tempRight in names):
                tempRight = names[tempRight]
            elif(type(tempRight)!= str):
                tempRight = self.right.eval()
        else:
            if(tempRight in names.values()):
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
        if(len(stack)>0):
            if(type(self.left)!=list):
                if(self.left in stack[len(stack)-1]["names"]):
                    tempLeft = stack[len(stack)-1]["names"][self.left]
            else:
                if(self.left in stack[len(stack)-1]["names"].values()):
                    tempLeft = stack[len(stack)-1]["names"][self.left]

        if(type(self.left)!=list):       
            if(self.left in names):
                tempLeft = names[self.left]
            elif ((not isinstance(tempLeft, int)) and (not isinstance(tempLeft,float))):
                tempLeft = self.left.eval()
        else:
            if(self.left in names.values()):
                tempLeft = names[self.left]
            elif ((not isinstance(tempLeft, int)) and (not isinstance(tempLeft,float))):
                tempLeft = self.left.eval()

        if(len(stack)>0):
            if(type(self.right)!=list):
                if(self.right in stack[len(stack)-1]["names"]):
                    tempRight = stack[len(stack)-1]["names"][self.right]
            else:
                if(self.right in stack[len(stack)-1]["names"].values()):
                    tempRight = stack[len(stack)-1]["names"][self.right]

        if(type(self.right)!=list):        
            if(self.right in names):
                tempRight = names[self.right]
            elif ((not isinstance(tempRight, int)) and (not isinstance(tempRight,float))): #DOUBLE CHECK THAT THESE ARE THE ONLY ONES THAT CAN BE PASSE
                tempRight = self.right.eval()
        else:
            if(self.right in names.values()):
                tempRight = names[self.right]
            elif ((not isinstance(tempRight, int)) and (not isinstance(tempRight,float))): #DOUBLE CHECK THAT THESE ARE THE ONLY ONES THAT CAN BE PASSE
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
        inStack =0
        global names
        tempRight = self.right
        tempLeft = self.left

        
        #I check if the stack has more than 1 element in it
        if(len(stack)>0):
            #if the right is a name itself
            if(type(tempRight)!=list):
                if(tempRight in stack[len(stack)-1]["names"]):
                    tempRight = stack[len(stack)-1]["names"][tempRight]
            else:
                if(tempRight in stack[len(stack)-1]["names"].values()):
                    tempRight = stack[len(stack)-1]["names"][tempRight]
        
        if(len(names)!=0):
            if(type(tempRight)!=list):           
                if (tempRight in names):
                    tempRight = names[tempRight]
            else:
                if (tempRight in names.values()):
                    tempRight = names[tempRight]
        

        if(type(tempRight)==str):
            if((tempRight[0] != "\"") and (tempRight[0]!= "'")):
                raise sbml_lexer.SemanticError()

        #if the stack is greater than 1
        if(len(stack)>0):
            if(type(tempRight)!=int):
                if(type(tempRight)!=list): 
                    if (tempRight in stack[-1]["names"]):
                        stack[len(stack)-1]["names"][tempLeft] = stack[len(stack)-1]["names"][tempRight]
                    else:
                        while(primTypeCheck(tempRight)==False):
                            tempRight = tempRight.eval()
                        stack[-1]["names"][tempLeft] = tempRight
                else:
                    if (tempRight in stack[-1]["names"].values()):
                        stack[len(stack)-1]["names"][tempLeft] = stack[len(stack)-1]["names"][tempRight]
                    else:
                        while(primTypeCheck(tempRight)==False):
                            tempRight = tempRight.eval()
                        stack[-1]["names"][tempLeft] = tempRight
            else:
                stack[len(stack)-1]["names"][tempLeft] = tempRight

            inStack = 1

        if(inStack==0):
            if(type(tempRight)!=int):
                if(type(tempRight)!=list): 
                    if (tempRight in names):
                        names[tempLeft] = names[tempRight]
                    else:
                        names[tempLeft] = tempRight.eval()
                else:
                    if (tempRight in names.values()):
                        names[tempLeft] = names[tempRight]
                    else:
                        names[tempLeft] = tempRight.eval()
            else:
                names[tempLeft] = tempRight


class printNode:
    def __init__(self, value):
        self.value = value

    def eval(self):
        found = 0
        val = self.value
        if(not isinstance(val, str)): 
            val = self.value.eval()

        if(len(stack)>0):
            if(type(val)!=list):
                if(val in stack[len(stack)-1]["names"]):
                    print(stack[len(stack)-1]["names"][val])
                    found =1
            else:
                if(val in stack[len(stack)-1]["names"].values()):
                    print(stack[len(stack)-1]["names"][val])
                    found =1
        if (found ==0):
            if(type(val)!=list):
                if (val in names):
                    print(names[val])
                else:
                    print(val)
            else:
                if (val in names.values()):
                    print(names[val])
                else:
                    print(val)                

class ifNode:
    def __init__(self,value, block):
        self.value = value
        self.block = block

    def eval(self):
        val = self.value
        if(len(stack)>0):
            if(type(val)!=list):
                if(val in stack[len(stack)-1]["names"]):
                    val = stack[len(stack)-1]["names"][val]
            else:
                if(val in stack[len(stack)-1]["names"].values):
                    val = stack[len(stack)-1]["names"][val]
        if(type(val)!=list):
            if(val in names):
                val = names[val]
        else:
            if(val in names.values()):
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
        if(len(stack)>0):
            if(type(val)!=list):          
                if(val in stack[len(stack)-1]["names"]):
                    val = stack[len(stack)-1]["names"][val]
            else:
                if(val in stack[len(stack)-1]["names"].values):
                    val = stack[len(stack)-1]["names"][val]                
        
        if(type(val)!=list): 
            if(val in names):
                val = names[val]
            else:
                val = self.value.eval()
        else:
            if(val in names.values()):
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
        found = 0
        if(len(stack)>0):
            if(type(self.value)!=list): 
                if(self.value in stack[len(stack)-1]["names"]):
                    found = 1
                    while([self.value]):
                        self.block.eval()
            else:
                if(self.value in stack[len(stack)-1]["names"].values()):
                    found = 1
                    while([self.value]):
                        self.block.eval()                
        if(found==0):
            if(type(self.value)!=list): 
                if(self.value in names):
                    while(names[self.value]):
                        self.block.eval()
                else:
                    while(self.value.eval()):
                        self.block.eval()
            else:
                if(self.value in names.values()):
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

#function node
class funNode:
    def __init__(self, name, expressions, block, output):
        self.name = name
        self.expressions = expressions
        self.block =block
        self.output = output

        tempNames = {}
        # expressions = mid
        #make sure the name is a string

        if(type(name)!=str):
            raise sbml_lexer.SemanticError()

        fun_dict = {
            "funName": name,
            "expression": expressions,
            "block": block,
            "names" : tempNames,
            "output": output
        }

        tempStack.append(fun_dict)




class funCalledNode:
    def __init__(self, name, right):
        self.name = name
        self.right = right


    def eval(self):
        tempName = self.name
        tempRight = self.right


        for j in range(0,len(tempRight)):
            if(primTypeCheck(tempRight[j])==False):
                tempRight[j] = tempRight[j].eval()


        if(not isinstance(tempName,str)):
            # tempName.eval()
            raise sbml_lexer.SemanticError()

        found = 0

        for i in range(0, len(tempStack)):
            tempDic = copy.deepcopy(tempStack[i])
            #I see if there is a functin name for the one i'm looking for
            if(tempDic['funName'] == tempName):
                found = 1

                #I assign the local variable passed to the name associated with it 
                expressions = tempDic["expression"]

                #I check that the right number of expressions are passed

                if(len(expressions)!=len(tempRight)):
                    raise sbml_lexer.SemanticError()

                #I check if the expression is in the local variables
                if(len(stack)>0):
                    for j in range(0, len(tempRight)):
                        if(tempRight[j] in stack[len(stack)-1]["names"]):
                            tempRight[j] = stack[len(stack)-1]["names"][tempRight[j]]
                            # nameFound = 1

                #try to see if any parameters passed are in the global dictionary
                for j in range(0, len(tempRight)):
                    if(type(tempRight[j])!=list):
                        if(tempRight[j] in names):
                            tempRight[j] = names[tempRight[j]]
                    else:
                        if(tempRight[j] in names.values()):
                            tempRight[j] = names[tempRight[j]]
                
                dicNames = {}

                for j in range(0,len(tempRight)):
                    dicNames[expressions[j]] = tempRight[j]

                tempDic["names"] = dicNames

                #I push this onto the stack
                stack.append(tempDic)
                #I evaluate the element on the stack
                stack[len(stack)-1]["block"].eval()

                #get output
                outputName = stack[-1]["output"]
                outputValue = None
                if(type(outputName)!=list):
                    if outputName in stack[-1]["names"]:
                        outputValue = stack[-1]["names"][outputName]
                else:
                    if outputName in stack[-1]["names"].values():
                        outputValue = stack[-1]["names"][outputName]

                #I remove the last element of the list
                stack.pop()
                #I evaluate with the right parameter
                if (outputValue!= None):
                    return outputValue
                

        if (found ==0):
            # print("error raised in this spot")
            raise sbml_lexer.SemanticError()




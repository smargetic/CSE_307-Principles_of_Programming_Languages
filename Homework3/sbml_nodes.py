#Sabrina Margetic
#Student ID Number: 109898930

import sbml_lexer
import inspect


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
        if((value=="True") or (value =="False")):
            self.value = value
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
                    # if(isinstance(item,list)==False):
                    #     tempList.append(item.eval())
                    # else:
                    #     tempList.append(item)
                
                tupleTemp = tuple(tempList)
                return tupleTemp
            elif(count ==1):
                for item in self.value:
                    return tuple([item.eval()])
        else:
            return ()

    
class listIndex:
    def __init__(self, left, right):
        if(isinstance(left.eval(),str)or isinstance(left.eval(), list)):
            if(isinstance(right.eval(),int)):
                super().__init__()
                self.left = left
                self.right = right
            else:
                raise sbml_lexer.SemanticError()
        else:
            sbml_lexer.SemanticError()
    
    def eval(self):
        count = 0
        temp = []
        if (isinstance(self.left.eval(), str)):
            temp = list(self.left.eval())
        else:
            temp = self.left.eval()
        
        for item in temp:
            count = count + 1
        
        if ((count-1)<self.right.eval()):
            raise sbml_lexer.SemanticError()

        return temp[self.right.eval()]

class tupleIndex:
    def __init__(self, left, right):
        if(isinstance(left.eval(),int)):
            if(isinstance(right.eval(),tuple)):
                super().__init__()
                self.left = left
                self.right = right
            else:
                raise sbml_lexer.SemanticError()
        else:
            sbml_lexer.SemanticError()
    def eval(self):
        count = 0
        for item in self.right.eval():
            count = count + 1
        if ((count-1)<self.left.eval()):
            raise sbml_lexer.SemanticError()

        count2 = 0
        for item in self.right.eval():
            if count2==self.left.eval():
                return item
            count2 = count2 + 1

#OPERATORS
class Negation:
    def __init__(self, value):
        if(value == "True"):
            super().__init__()
            self.value = True
        elif (value == "False"):
            super().__init__()
            self.value = False
        else:
            raise sbml_lexer.SemanticError()

    def eval(self):
        return not self.value

class booleanConjDisj:
    def __init__(self, left, op, right):
        if(typeChecking(left, right)==True):
            if(left=="True"):
                super().__init__()
                self.left = True
            elif(left=="False"):
                super().__init__()
                self.left = False
            else:
                raise sbml_lexer.SemanticError()
            
            if(right=="True"):
                self.right = True
            elif(right=="False"):
                self.right = False
            else:
                raise sbml_lexer.SemanticError()
            self.op = op
        else:
            raise sbml_lexer.SemanticError()
    def eval(self):
        if(self.op =='andalso'):
            return self.left and self.right
        elif(self.op == 'orelse'):
            return self.left or self.right

        
class BinomialOp:
    def __init__(self, left, oper, right):
        if(typeChecking(left.eval(), right.eval())==True):
            super().__init__()
            self.left = left
            self.right = right
            self.oper = oper
            self.type = "binOp"
            if((oper =='-')and (numberCheck(left.eval(),right.eval())==False)):
                raise sbml_lexer.SemanticError()
            elif((oper == '+') and (not (isinstance(left.eval(), str) or numberCheck(left.eval(),right.eval()) or isinstance(left.eval(), list))) ):
                raise sbml_lexer.SemanticError()
            elif((oper == '*') and (numberCheck(left.eval(),right.eval())==False)):
                raise sbml_lexer.SemanticError()
            elif((oper == '/') and (numberCheck(left.eval(),right.eval())==False)):
                raise sbml_lexer.SemanticError()
            elif((oper == '**') and (numberCheck(left.eval(),right.eval())==False)):
                raise sbml_lexer.SemanticError()
            elif((oper=='div') and (not (isinstance(left.eval(), int) and isinstance(right.eval(), int)))):
                raise sbml_lexer.SemanticError()
            elif((oper=='mod') and (not (isinstance(left.eval(), int) and isinstance(right.eval(), int)))):
                raise sbml_lexer.SemanticError()

        else: 
            raise sbml_lexer.SemanticError()
    def eval(self):
        if (self.oper== '-'):
            return (self.left.eval()-self.right.eval())
        elif (self.oper=='+'):
            return (self.left.eval()+self.right.eval())
        elif (self.oper=='*'):
            return (self.left.eval()*self.right.eval())
        elif (self.oper=='/'):
            if(self.right.eval()==0):
                raise sbml_lexer.SemanticError()
            return float(self.left.eval())/float(self.right.eval())
        elif (self.oper=='**'):
            if(numberCheck(self.left, self.right)==False):
                raise sbml_lexer.SemanticError()  
            return (self.left.eval()**self.right.eval())
        elif (self.oper=='div'):
            return int(self.left.eval()/self.right.eval()) #DOUBLE CHECK HTIS
        elif(self.oper=='mod'):
            return (self.left.eval())%(self.right.eval())

class inOperator:
    def __init__(self, left, right):
        if(isinstance(right.eval(), list) or isinstance(right,tuple)):
            super().__init__()
            self.left = left
            self.right = right
        else: 
            raise sbml_lexer.SemanticError()
    def eval(self):
        return self.left.eval() in self.right.eval() #double check

class conjOperator:
    def __init__(self, left, right):
        if(typeChecking(left,right)==True):
            if(isinstance(left.eval(),list)):
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
        return tempList

class conjOperatorTuple:
    def __init__(self, left, right):
        if(typeChecking(left,right)==True):
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
        self.value = value.eval()
    def eval(self):
        return (self.value)
        # return "(" + str(self.value) + ")"


class ComparisonOp:
    def __init__(self, left, op, right):
        super().__init__()
        if(typeChecking(left.eval(), right.eval())==True):
            if(isinstance(left.eval(),str) or numberCheck(left.eval(), right.eval())):
                self.left = left
                self.left.parent = self
                self.right = right
                self.right.parent = self
                self.op = op
            else:
                raise sbml_lexer.SemanticError()
        else:
            raise sbml_lexer.SemanticError()


    def eval(self): 
        if (self.op=='<'):
            return (self.left.eval()<self.right.eval())
        elif(self.op=='>'):
            return (self.left.eval()>self.right.eval())
        elif(self.op=='<='):
            return (self.left.eval()<=self.right.eval())
        elif(self.op=='>='):
            return (self.left.eval()>=self.right.eval())
        elif(self.op=='=='):
            return (self.left.eval()==self.right.eval())
        elif(self.op=='<>'):
            return not(self.left.eval()==self.right.eval())

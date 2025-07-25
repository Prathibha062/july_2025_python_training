class Calculator:
    def __init__(self):
        print("this init")
    def add(self,a,b):
        return a+b
    def sub(self,a,b):
        return a-b
    def mul(self,a,b):
        return a*b
    def div(self,a,b):
        return a/b
    def action(self,action,a,b):
        if(action=="add"):
            return self.add(a,b)
        if(action=="sub"):
            return self.sub(a,b)
        if(action=="mul"):
            return self.mul(a,b)
        if(action=="div"):
            return self.div(a,b)
calc = Calculator()
action=input("enter the action")
num1=int(input("enter the number 1:"))
num2=int(input("enter the number 2:"))
result=calc.action(action,num1,num2)
print(result)


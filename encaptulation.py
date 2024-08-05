class calculator:
   def __init__(self,op1,op2):
        self.op1=op1
        self.op2=op2
   def add(self):
       return self.op1+self.op2
   def sub(self):
       return self.op1-self.op2
   
calc=calculator(20,10)
result=calc.add()
print("addition is:",result)

result=calc.sub()
print("substraction is:",result)
        
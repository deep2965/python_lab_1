class company:
    def getinfo(self):
        self.name=input("enter name of company:")
        self.city=input("enter city:")
        self.mobile_no=input("enter mobile_no:")
        self.emp_name=input("enter emp_name:") 
        self.designation=input("enter designation:") 
        self.salary=input("enter salary:") 

    def printinfo(self):
        print("name:",self.name,  "city:",self.city,"mobileno:",self.mobile_no,"emp_name:",self.emp_name,"designation:",self.designation,"salary:",self.salary)

    
class employee(company):
    def getdata(self):
        self.getinfo()
    def setdata(self):
        self.printinfo()

s=employee()
s.getdata()
print("--information--")
s.setdata()
class employee:
    name=""
    dateofjoin=""
    designation=""
    salary=""
    
    def setdata(self,name,dateofjoin,designation,salary):
        self.name=name
        self.dateofjoin=dateofjoin
        self.designation=designation
        self.salary=salary

    def display(self):
        print("name:",self.name)
        print("dateofjoin:",self.dateofjoin)
        print("designation:",self.designation)
        print("salary:",self.salary)

def main():
    emp=employee()
    emp.setdata('abc','20 feb 2024','manager',50000)
    emp.display()

if __name__=="__main__":
    main()

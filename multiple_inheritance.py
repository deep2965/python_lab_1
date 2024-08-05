class firstname:
    def getdata(self):
        print("abc")

class lastname:
    def retrivedata(self):
        print("sharma")

class fullname(firstname, lastname):
    pass
print("--full name is--")
b1 = fullname()

b1.getdata()
b1.retrivedata()
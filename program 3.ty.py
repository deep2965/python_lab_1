a=input ("enter name:")
b=int(input("enter roll no.:"))
print("enter marks outof 100")
java=int (input("java marks:"))
seo=int (input("seo marks:"))
php=int (input ("php marks:"))
sad=int(input("sad marks:"))
python=int (input("python marks:"))
if(java>30 and seo>30 and php>30 and sad>30 and python>30):
    total=java+seo+php+sad+python
    print("Total is:", total)
    per=total/5
    print ("percentage is:" ,per) 
    if(per>=90):
        print("Grade :A")
    elif(per<90 and per>=70):
        print("Grade :B")
    elif(per>70 and per<=60):
        print("Grade :C")
    elif(per>60 and per<=50):
        print ("Grade :D")
    else:
        print("Better luck next time")
else:
    print("YOU ARE FAIL")
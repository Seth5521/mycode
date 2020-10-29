

#num1= float(input("Choose a number."))
#num2= float(input("Choose a second number."))
#def add(x,y):
   # print(x+y)
# +,-,*,/
#if answer == "+":
# add(num1,num2)



num1= float(input("Pick a number.  "))
num2= float(input("Pick another number.  "))
p1= input("Choose: add, subtract, multiply, or divide  ").lower()


def dothis(a,b):
    if p1 == "add":
        print(a+b)
    elif p1 == "subtract":
         print(a-b)
    elif p1 =="multiply":
         print(a*b)
    elif p1 =="divide":
        print(a/b)





dothis(num1,num2)

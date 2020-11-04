#!/usr/bin/env python3

def q1():
    print("Are you hungry? ")
    ans= (input("YES or NO"))

    if ans.lower() == "no":
        print("Yes you are.")
        print("Have a slice of pizza.")
    elif ans.lower() == "q":
        print("Goodbye.")
        exit()
    elif ans.lower() == "yes":
        q2()
    else:
        print("Please answer yes or no")
        q1()
def q2():
    print("Do you want to eat healthy? ")
    ans=input("YES or NO")

    if ans.lower() == "yes":
        print("No you don't.")
        print("Have a slice of pizza.")
    elif ans.lower() == "q":
        print("Goodbye.")
    elif ans.lower() == "no":
        print("Of course not")
        print("Have a slice of pizza.")
    else:
        print("Please answer yes or no")
        q2() 
if __name__ == "__main__":
        q1()




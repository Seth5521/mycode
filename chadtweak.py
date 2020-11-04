#!/usr/bin/env python3

def q1():

    while True:
        print("Are you hungry? ")
        ans= (input("YES or NO"))

        if ans.lower() == "no":
            print("Yes you are.")
            print("Have a slice of pizza.")
            break
        elif ans.lower() == "q":
            print("Goodbye.")
            break
        elif ans.lower() == "yes":
            q2()
            break
        else:
            print("Please answer yes or no")
def q2():
        
    while True:
        print("Do you want to eat healthy? ")
        ans=input("YES or NO")

        if ans.lower() == "yes":
            print("No you don't.")
            print("Have a slice of pizza.")
            break
        elif ans.lower() == "q":
            print("Goodbye.")
            break
        elif ans.lower() == "no":
            print("Of course not")
            print("Have a slice of pizza.")
            break
        else:
            print("Please answer yes or no")
            print (q2()) 

if __name__ == "__main__":
        q1()




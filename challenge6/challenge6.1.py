#!/usr/bin/env python3
def seth():    
    for x in range(1,6):
        print(x*"* ")
    for x in range(4,-1,-1):
        print(x*"* ")

    star = ["*"]
    for x in star:
            for y in range(1,6):
               print(y*x)
    print()

seth()

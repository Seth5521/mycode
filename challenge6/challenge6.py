#!/usr/bin/env python3

item = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

for x in item:
    print("*")
    while x in item:
        sleep(1.5)
        print("*")

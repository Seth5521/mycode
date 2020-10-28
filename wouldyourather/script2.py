#!/usr/bin/env python3

print('Please choose your answer by typing the capitalized phrase from the question.')
print('Would you rather:')
question1 = 'empty'
# wrap connection in a float() to accept decimals as numbers
question1=input("TRAVEL abroad or STAY at home?")

if question1.lower() == 'travel':
    print('Good luck with that right now')
elif question1.lower() == 'stay':
    print('Seems kinda lame, but I guess thats cool...')
elif question1.lower() == 'neither':
    print('Okay wierdo.')
else:
    print("That wasn't an option silly goose!")

#!/usr/bin/python3


#printing the question to the user
import time
import random

print("What is your quest?")
quest=input()
quest.replace("my","your")
#find out out to change "my" to "your" for output
quest=(quest.replace("my", "your"))
print(f"You seek {quest}?")

#cool list maybe we can figure out something neat to do with it.
item_list = ["sword", "rope", "elixir", "poison", "dragon's tooth"]
animal_list = ["donkey", "chicken", "horse", "deer", "rat", "dragon"]

time.sleep(2)

print(f"The stranger gives you a quizzical look before eyeing your {random.choice(item_list)} so you cover it with your cloak.")

time.sleep(2)

print(f"The stranger asks 'will you take your {random.choice(animal_list)} with you?'")

companion_animal=input()


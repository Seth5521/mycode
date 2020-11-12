#!/usr/bin/python3

import time
import random
from random import seed
from random import randint

def time_date():
    first_value = str(randint(0, 23))
    second_value = str(randint(0, 5))
    third_value = str(randint(0,9 ))
    fourth_value  = str(randint(0, 0))
    fifth_value = str(randint(1, 12))
    sixth_value = str(randint(1,31))
    print(first_value+":"+second_value + third_value, fifth_value+"/"+sixth_value)

#defining answers to help manipulate output
negative_answer = "no"
positive_answer = "yes"
my_answer = "my"
your_answer = "your"
yeah_answer = "yeah"
nope_ans = "nope"
you_ans = "you"
prob_ans = "probably"
#print("It is currently", time_date())

#prompting the first question to the user
print("What is your quest?")
quest=input()
if my_answer in quest:
    quest = quest.replace("my","your")
elif your_answer in quest:
    quest = quest.replace("your","my")
elif you_ans in quest:
    quest = quest.replace("you", "me")

#reiterating user input
print(f"You seek {quest}?")

#cool lists maybe we can figure out something neat to do with it.
item_list = ["sword", "rope", "elixir", "poison", "dragon's tooth"]
animal_list = ["donkey", "chicken", "horse", "deer", "rat", "dragon"]
day = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
occurence = ["fisrt", "second", "third", "fourth"]
tod = ["morning", "afternoon", "evening", "night"]
time_desc = ["late", "early"] 
standing1 = ["an alleyway", "a field","your driveway", "literally the worst pothole ridden street in America", "the parking lot of a costco"]
sky_desc = ["cloudy", "clear", "bright", "dark", "a shade of purple", "very high up there"]
feeling1 = ["hungry", "tired", "concerned", "lazy", "a rush of energy", "like you are forgetting something"]
dogtype = ["Pomeranian", "Husky", "Golden Retriever", "Bulldog", "Poodle", "Chihuahua", "German Shepherd", "Cocker Spaniel"] 
dogname = ["Foxy", "Barbie", "Cano", "Frank", "Zelda", "Gunter", "Spot", "Cheech", "Buddy", "Charlie"]
person1 = ["uncle", "brother", "cousin", "best friend", "old roommate", "guidance counselor", "probation officer", "sister's boyfriend"]
name1 = ["John", "Mark", "Tyler", "Blake", "Jesus", "Mork", "Frodo", "James", "William", "Paddy"]
time1 = ["first", "last", "only"]
event1 = ["went canoeing", "ran a 5k", "challenged the sixth graders to a game of 21", "volunteered at the homeless shelter", "scalped tickets to a Mystics game", "prank called 911", "went to a white elephant party"]
quote1 = ['"I aint afraid of no ghosts"', '"beauty is just a light switch away"', '"Maybe we shouldnt hang out anymore"', '"I 100% regret bringing you with me"', '"I am super scared right now"', '"Maybe we dont do this again"']
color1 = ["yellow", "red", "pink", "blue", "burgundy", "white", "black", "green", "orange", "gray", "purple"]
car1 = [ "Camaro", "Dodge Neon", "Toyota Camry ", "Cadillac", "Honda Odysee", "Firetruck", "Volkswagen Bug", "Jeep Grand Cherokee", "Volkswagen Jetta"] 
sticker1 = ["'My other ride is crippling depression'", "'Baby on board'", "'Your local police are armed and dangerous'", "'Legalize It!'", "'From here I can see Urnanus'", "'My girlfriends' husband fights for your freedom'", "'I still consider Pluto a planet'"]
thought1 = ["I need to leave immediately", "At least i'm not as dumb as that guy", "do they think thats funny?", "Maybe I will move to Canada after all", "I should really be friends with that person", "If they do a U-turn I need to run"]
event2 = ["band practice", "to give your cat her heart medication", "to pick up your mountain bike from the shop", "to watch Famiy Fued", "a zoom meeting with your ex", "to see a man about a horse", "irritable bowel syndrome", "lost all grip on reality"]
choice1 = ["call an Uber", "unleash the dog and take off running", "head to the bus stop", "call your mom for a ride",]
location1 = ["Home Depot", "the gas station", "Jeremy's house", "the soup kitchen", "Trader Joe's", "Safeway", "the gym"]
item2 = ["vegan beef jerkey", "soup that isn't terrible", "seven different kinds of superglue", "the best spicy snacks", "a mall Santa witha funny lisp", "free nachos", "a 'child size' smoothie that is actually the size of a toddler", "pizza without the crust"]
choice2 = ["you should really start taking your medication", "its too late to start a movie", "youre going to mow the lawn tomorrow", "you can totally smell the curry you cooked last night", "it's time to replace the batteries in the smoke detectors"]
action1 = ["creep", "slither", "sprint", "slide", "low crawl", "frolic", "moonwalk", "walk backward"]
bedtime1 = ["to cry yourself to sleep", "for the nightmare to continue", "for sleep paralysis and night sweats", "for a nice nap", "to think about all the embarrasing things youve ever done or said", "to close your eyes and lay still for a few hours", "to panic about your eye exam scheduled for tomorrow", "to plan your world domination"]
time.sleep(2)

print(f"The stranger gives you a quizzical look before eyeing your {random.choice(item_list)} so you cover it with your cloak.")

time.sleep(2)

rand_anim = random.choice(animal_list)
print(f"The stranger asks 'will you take your", rand_anim, "with you?'")

companion_animal=input().lower()
if yeah_answer in companion_animal:
   companion_animal = companion_animal.replace(yeah_answer, positive_answer)

comp_anim = companion_animal.split()

if nope_ans in comp_anim:
    print("NOICE!")
if negative_answer in comp_anim:
    print("NOICE!")
if prob_ans in comp_anim:
    print("yOu pRoBaBly sHoULdnT")
if positive_answer in comp_anim:
    print("Very unwise, but you do you I guess.")
    

time.sleep(2)
print(r"""

 _____   _             _               
|  _  |_| |_ _ ___ ___| |_ _ _ ___ ___ 
|     | . | | | -_|   |  _| | |  _| -_|
|__|__|___|\_/|___|_|_|_| |___|_| |___|
   _____ _                             
  |_   _|_|_____ ___                   
    | | | |     | -_|                  
    |_| |_|_|_|_|___|                  
                              
                """)
time.sleep(3)

print(f"It is the {random.choice(occurence)} {random.choice(day)} of the month and {random.choice(time_desc)} in the {random.choice(tod)}.")
print()
if positive_answer in comp_anim:
    print(f"The", rand_anim, "looks up at you, and you already regret your decision.")
elif prob_ans in comp_anim:
    print(f"just as the strange person had said you probably shouldnt have brought the", rand_anim, ".")
time.sleep(7)
print()
print(f"You are standing in {random.choice(standing1)}, you look at the sky and it is {random.choice(sky_desc)} and you feel {random.choice(feeling1)}.")
time.sleep(10)
print()
print(f"You were daydreaming again, something about a stranger and a quest?? back to reality you're walking youre neighbors {random.choice(dogtype)} {random.choice(dogname)}, not a", rand_anim, "at all.")
time.sleep(11)
print()
print(f"You start to think about your {random.choice(person1)} {random.choice(name1)} and what he told you the {random.choice(time1)} time both of you {random.choice(event1)} : \n {random.choice(quote1)} and your starting to question if you remembered that correctly and what made you think of this right now.")
time.sleep(15)
print()
print(f"A {random.choice(color1)} {random.choice(car1)} drives by and you squint to read its faded bumper sticker {random.choice(sticker1)} it reads, and you think to yourself : {random.choice(thought1)}.")
time.sleep(12)
print()
print(f"You just remembered you have {random.choice(event2)} and you must get home. Because you are running late you choose to {random.choice(choice1)}.\n On your way back you make a pit stop at {random.choice(location1)} because they have {random.choice(item2)} and you can't pass on that.")
time.sleep(15)
print()
print(f"Once back at your house you decide {random.choice(choice2)} \n  you {random.choice(action1)} into your bedroom, lay down on your bed and know its time {random.choice(bedtime1)}.") 

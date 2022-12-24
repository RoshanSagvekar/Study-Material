import random
import math
from typing import Counter

# Taking Inputs For Lower and Upper Limit
username=input('Enter Your Name:')
lower=int(input('Enter Lower Limit:'))
upper=int(input('Enter Upper Limit:'))

# Generating random number between Upper And Lower Limit
num=random.randint(lower,upper)
chance=round(math.log(upper-lower+1,2))
print('You have ',chance,' chances to guess number.')

count=0
while count<chance:
    count+=1
    guess=int(input('Guess the Number:-'))
    if num == guess:
        print("\tHurray!!")
        print("\tCongratulations,"+username+" you did it in ",count, " try.")
        # Once guessed, loop will break
        break
    elif num > guess:
        print("You guessed too small!")
    elif num < guess:
        print("You Guessed too high!")

if count >= chance:
    print("\nThe number is %d" %num)
    print("\tBetter Luck Next time!")
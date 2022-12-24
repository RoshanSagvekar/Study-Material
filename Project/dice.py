'''import random
while True:
    print('1.Roll the Dice\n2.Exit')
    user=int(input('What do you want to do?\n'))
    if user==1:         
        number = random.randint(1,6)         
        print(number)     
    else:         
        break
'''

# No Guessing Logic
import random
number = random.randint(1,10)
for i in range(0,1):
    user = int(input("guess the number="))
    if user == number:
        print("Hurray!!")
        print(f"you guessed the number right it's {number}")
        break
if user != number:
    print(f"Your guess is incorrect the number is {number}")



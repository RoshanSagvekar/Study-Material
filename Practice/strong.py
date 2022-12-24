'''Write a program to Check and Display if the number is Strong or not.
a. Sum of factorial of it Digits equal to that number is known
As a Strong Number.
e.g.
145 = 1! + 4! + 5!
= 1 + 24 + 125
= 145'''

num=int(input('Enter a Number:'))
temp=num
sum=0
while num>0:
    digit=num%10
    fact=1
    for i in range(1,digit+1):
        fact=fact*i
    sum=sum+fact
    num=num//10
if sum==temp:
    print(temp,'is a Strong number.')
else:
    print(temp,'is not a Strong number.')

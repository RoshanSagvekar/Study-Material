#Write a Program to accept 2 numbers from the user and Display Lowest number,
#if both are equal display 2nd number is lowest.

n1=int(input('Enter a Number='))
n2=int(input('Enter a Number='))
if(n1>n2) or (n1==n2):
    print(n2,'is the lowest number.')
else:
    print(n1,'is the lowest number.')
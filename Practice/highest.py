# Write a Program to accept 2 numbers from the user and Display highest number,
# if both are equal display 1st number is highest.

n1=int(input('Enter a Number='))
n2=int(input('Enter a Number='))
if(n1>n2) or (n1==n2):
    print(n1,'is the highest number.')
else:
    print(n2,'is the highest number.')


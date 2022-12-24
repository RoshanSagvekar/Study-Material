'''
Write a program to Display Number which satisfied following Conditions (Note
entered number must be between 33 to 99).
E.g
The number is 45
Its Square is 2025
Sum of 1st 2 digit and last 2 digit is 20 + 25 =
'''

num=int(input('Enter a Number(between 33 to 99)='))
sq=num*num
print('Square of ',num,':',sq)
sum=0
while sq>0:
    digit=sq%100
    sum=sum+digit
    sq=sq//100
print('Sum of 1st 2 digit and last 2 digit of square is=',sum)
    

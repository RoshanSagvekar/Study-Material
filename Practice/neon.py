'''
Write a program to check whether a given number is Neon Number or not.
A Neon number is a number where the sum of digits of the square of
the number is equal to the number.
a. If entered number is between 1 to 32
E.g
1. The number is 9.
Its square is 81
Sum of digits of the square is 8 + 1 = 9
2. The Number is 12 (Not Neon Number)
Its square is 144
Sum of digits of the square is 1 + 4 + 4 = 9
'''

num=int(input('Enter A Number='))
sq=num*num
print('Square of',num,'is',sq)
sum=0
while sq>0:
    digit=sq%10
    sum=sum+digit
    sq=sq//10
print('Sum of digits of the square is',sum)
if sum==num:
    print(num,'is a neon number')
else:
    print(num,'is not a neon number.')
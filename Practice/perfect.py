'''
Write a program to Check and Display the number is Perfect or not.
A Perfect number is a positive integer that is equal to the sum of its
positive divisors, excluding the number itself.
For instance, 6 has divisors 1, 2 and 3, and 1 + 2 + 3 = 6, so 6 is a perfect
number.
'''
num=int(input('Enter a Number='))
sum=0
for i in range(1,num):
    while num%i==0:
        sum=sum+i
        break
print('Sum of positive divisor of',num,'=',sum)
if sum==num:
    print(num,'is a perfect number.')
else:
    print(num,'is not a perfect number.')
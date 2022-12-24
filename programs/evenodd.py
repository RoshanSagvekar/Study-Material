#WAP to accept a number from user and print it if it is odd or even?
#if number is divide by 2 and remainder is 0 then it is call even number.
#if number is divide by 2 and remainder is 1 then it is call odd number.

num=int(input('Enter a Number='))
if num%2==0:
    print(num,' is Even Number.')
else:
    print(num,' is Odd Number.')
print('Program execution is completed.')

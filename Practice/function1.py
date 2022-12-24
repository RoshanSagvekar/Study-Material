#Write a function to display sum of digits of given number

def sumofdigit(num):
    sum=0
    while num>0:
        digit=num%10
        sum=sum+digit
        num=num//10
    return sum

n=int(input('Enter a number:'))
print('Sum of digits of number=',sumofdigit(n))
#WAP to accept a number from user and check whether it is divisible by 3 and 5.

num=int(input('Enter a Number='))
if(num%3==0 and num%5==0):
    print(num,'is divisible by 3 and 5')
elif(num%3==0 and num%5!=0):
    print(num,'is divisible by only 3')
elif(num%3!=0 and num%5==0):
    print(num,'is divisible by only 5')
else:
    print(num,'is not divisible by 3 and 5')
    
#WAP to reverse a number using while loop

num=int(input('Enter a number='))
temp=num
rev=0
while num>0:
    digit=num%10
    rev=rev*10+digit
    num=num//10
print('Reverse of',temp,'=',rev)
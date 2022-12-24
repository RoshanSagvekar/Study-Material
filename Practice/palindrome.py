#WAP to check number palindrome or not using while loop

num=int(input('Enter a number='))
temp=num
rev=0
while num>0:
    digit=num%10
    rev=rev*10+digit
    num=num//10
print('Entered Number=',temp)
print('Reverse of Number=',rev)
if(temp==rev):
    print(temp,'is a palindrome number.')
else:
    print(temp,'is not a palindrome number.')
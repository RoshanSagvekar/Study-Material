#Write a Program to accept a number count it's even and odd number of digits.
num=int(input('Enter a Number='))
evencnt=0
oddcnt=0
while num>0:
    digit=num%10
    if digit%2==0:
        evencnt+=1
    else:
        oddcnt+=1
    num=num//10
print('No. of even digits present in number=',evencnt)
print('No. of odd digits present in number=',oddcnt)

#Write a Program to accept a number count it's Number of Zero digits

num=int(input('Enter a number:'))
count=0
while num>0:
    digit=num%10
    if digit==0:
        count+=1
    num=num//10
print('Count of 0 in a number=',count)
#WAP to check number is armstrong or not

num=int(input('Enter a number='))
power = len(str(num))
num1=num
sum=0
while num>0:
    digit=num%10
    sum=sum+digit**power
    num=num//10
if(num1==sum):
    print(num1,'is a Armstrong Number')
else:
    print(num1,'is not a Armstrong Number')


#While loop
'''
    While loop is used to repeat a block of code.
    Instead of executing code blockonce
    While lopp executes the code block multiple times until condition
    becomes false.

    Syntax:
        initialize loop
        while condition:
            statements to be execute.
            increment/decrement
'''
'''
#E.g
cnt=0   #initialization
while(cnt<5):      #condition
    print('Hi')
    cnt+=1          #iteration statement
'''
'''
        ---#-Dry Run Table-#----

cnt     cnt<5       o/p
0       0<5(T)      Hi
1       1<5(T)      Hi
2       2<5(T)      Hi
3       3<5(T)      Hi
4       4<5(T)      Hi
5       5<5(F)
'''
'''
#WAP to accept a number from a user and count no.of digit?
n=int(input('Enter a Number='))
cnt=0
while(n>0):
    n=n//10
    cnt+=1
print('No .of digits=',cnt)
'''

#WAP to count the even number of digit?
'''
num=int(input('Enter a Number='))
cnt=0
while(num>0):
    rem=num%10
    if(rem%2==0):
        cnt+=1
    num=num//10
print('No .of Even digits=',cnt)

#2nd Way

num = int(input('Enter Number='))
num1= num
cnt = 0
while num>0:
    if(num%2==0):
        cnt+=1
    num=num//10
print('Number of even digits in',num1,' are ',cnt)
'''

#WAP to accept a no. from user and print it reverese?
'''
num=int(input("Enter a number="))
num1=num
rev=0
while num>0:                #123>0(T),  12>0(T) ,   1>0(T),     0>0(F)
    digit=num%10            #    3          2           1
    rev=rev*10+digit        #    3          32         321
    num=num//10             #    1          1           0
print('Reverse of',num1,' is',rev)
'''

#while loop with break and continue.
'''
print('Break with While Loop')
i=1
while i<=5:
    if i==3:
        break
    print(i)
    i+=1

print('Continue with While Loop')
i=0
while i<5:
    i+=1
    if i==3:
        continue
    print(i)

i=1
while i<5:
    if i==3:
        i+=1
        continue
        i+=1
    print(i)
    

'''

#WAP to accept a number from user and check whether it is palindrome or not?
'''
num=int(input("Enter a number="))
num1=num
rev=0
while num>0:            
    digit=num%10
    rev=rev*10+digit
    num=num//10
if(num1==rev):
    print(num1,'is a Palindrome number')
else:
    print(num1,'is not a Palindrome number')
'''
#WAP to check the given no. is armstrong or not. 
'''
num=int(input('Enter a number='))
num1=num
sum=0
while num>0:
    digit=num%10
    sum=sum+digit**3
    num=num//10
if(num1==sum):
    print(num1,'is a Armstrong Number')
else:
    print(num1,'is not a Armstrong Number')
'''

#else with while
'''
i=1
while i<=5:
    if i==7:
        break
    print(i)
    i+=1
else:
    print('While loop is execute without break statement')'''


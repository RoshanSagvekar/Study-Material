'''
s1 = 'ITVedant'
print("\nstr Iteration")
for letter in s1:
    print(letter,end=', ') 


l1 = [1,6,'Raj',[12,36],'Jay',21]
print("\nList Iteration")
for element in l1:
    print(element,end=', ')

t=(1,2,3,4) 
print("\nTuple Iteration")
for element in t:
    print(element, end=",")

'''
#As you all know str,list,and tuple are allowed indexing.
#How to create the sequence of number of specific range 1-10

'''
    Python provide a one built in function to create sequence of 
    number with specific range that function is known as range()
    syntax:-
        range(start,end,step)
        here
        start and step are optional withdefault value 0 and 1 respectively

        start :-define min value of sequence.
        end:-define max value of sequence( end value is excluded).
        step:-define the diference between the to value.
'''
'''
#e.g
print('Range(0,10,1')
for num in range(0,10,1):
    print(num,end=' ')

print('\nRange(0,10,1)')
for num in range(0,10,1):
    print(num,end=' ')

print('\nRange(2,30,3)')
for num in range(2,30,3):
    print(num,end=' ')


#WAP to print the sequence number from 30 to 1.
print('\nRange(30,1,1)')
for num in range(30,0,-1):
    print(num,end=' ')

'''
'''
#WAP to print the table of number enter by user?
#table format --> 2*1=2
n=int(input('Enter a number='))
for i in range(1,11):
    print(n,'x',i,'=',n*i)
'''
'''
#WAP to print the numbers between 1 to n those are divisible by m?

n=int(input('Enter a limit number = '))
m=int(input('Enter a divisible number='))
for num in range(1,n+1):
    if(num%m==0):
        print(num,end=',')
print("\nWithout modulus operator")
for num in range(m,n+1,m):
    print(num,end=',')


#WAP to accept string from user and its vowel?

name=input('Enter a string=')
count=0
for vowel in name:
    if vowel in 'aeiouAEIOU':
        count+=1 #Short hand operator for count=count+1
print('Number of vowel present in string is',count)

'''

#Break and continue keywords with loop(for,while)
'''
    break is a keyword of python programming which use to terminate the loop.
    if specified condition is satisfied.

print('\nExample of break Keyword')
for i in range(1,10):
    if i==5:
        break
    print(i,end=',')
'''
#Continue Keyword
'''
    Continue is also the keyword used to terminate the  current 
    iteration of for loop and while loop and continue with next expression.

print('\nExample of continue Keyword')
for i in range(1,10):
    if i==5:
        continue
    print(i,end=',')
'''

#WAP to skip the numbers from 5 to 15 from 1 to 20.
'''
for i in range(1,21):
    if i>=5 and i<=15:
        continue
    print(i,end=',')

for i in range(1,21):
    if i>4 and i<16:
        continue
    print(i,end=",")

for i in range(1,21):
    if 5<=i<=15:
        continue
    print(i,end=',')

for i in range(1,21):
    if i in range(5,16):
        continue
    print(i,end=',')

'''
#Looping statement with else statement
'''
    for with else statement
    Python allows us to use the else statements with for loop or 
    while loop.

    The else block of code just executed after the while/for loop
    only if the loop is not terminated by the break statement.

print('\nFor Without Break')
for i in range(1,10):
    print(i,end=',')
else:
    print('\nLoop is successfully Completed.')

print('\nFor With Break')
for i in range(1,10):
    if i==5:
        break
    print(i,end=',')
else:
    print('\nLoop is successfully Completed.')

'''
#WAP to check the given number is prime or not?
'''
num=int(input('Enter a number='))
for i in range(2,num):
    if num%i==0:
        print('The Number is not Prime.')
        break
else:
    print(num ,'is Prime Number')


num=int(input('Enter a number'))
flag=0
for i in range(2,num/2):
    if num%i==0:
        flag=1
        break
if flag==0:
    print(num,' is prime')
else:
    print(num,' is not prime')
'''

#WAP program to print addition of 1 to n numbers
n=int(input('Enter a number='))
sum=0
for num in range(1,n+1):
    sum=num+sum
print('Addition of 1 to',n,'numbers=',sum)

#WAP program to print factorial numbers entered by users?
'''
n=int(input('Enter a number='))
fact=1
for i in range(1,n+1):
    fact=fact*i
print('Factorial of ',n,'=',fact)
'''


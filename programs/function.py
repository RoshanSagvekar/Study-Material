#Script Programming(Vb.Script)
#Procedure Oriented Programming (C)
#Procedure is also known as Function.

#FUNCTION PROGRAMMING IN PYTHON

#What is Function?
'''
    ->Function is a group of related statements that performs specific
    task as per the requirement.

    ->It helps to save the logic of specific task.
'''
#Why we create a Function?
'''
    ->Functions helps to break the program into smaller parts.

    ->It helps to manage the code in more organize way.

    ->Function avoid repeatation of code and makes the code reusable.
'''
#Syntax
'''
Function Creation:

    def function_name(parameters/Argument):
        statements to be executed
        return value

To call/invoke Function
    
    function name(values)
'''


'''
Based on Parameters and Return Statement we can create a function
in python with following style.
''' 
#Function Writing Style.
#1.No Parameter with No returns
    # e.g above example sayhi()
'''
def sayhi():
    print('Hi Everyone!')
    print('\tWelcome To Python Programming.')
    print('\tThis is Function demo.')
    return 'Test'
sayhi()
print(sayhi())
'''

#2.Parameter with no return value.
    #e.g Addition of numbers
'''
def addition(n1,n2):
    print('Additon:-',n1+n2)

addition(12,52)
print(addition(50,50))
'''
#3.Parameter with return value.
    #e.g Addition of numbers
'''
def addition(n1,n2):
    return n1+n2
print('Addition:-',addition(3,9))

n1=int(input('Enter a Number='))
n2=int(input('Enter a Number='))
ans=addition(n1,n2)
print(n1,'+',n2,'=',ans)
'''
#WAP to create function to calculate square of number using parameter with no returns.
'''
def square(n):
    print('Square=',n*n)

square(4)
'''
#WAP to create function to calculate cube of number using parameter with returns.
'''
def Cube(n):
    return n**3
a=int(input('Enter a Number='))
cu=Cube(a)
print('Cube of',a,'=',cu)
'''

#4.No parameter with return
'''
def sayWelcome():
    return"Welcome To Python Programming!"
print('Hello,Student',sayWelcome())
print('Hello,Rosh',sayWelcome())
print('Hello,Max',sayWelcome())
'''

#Function calling with keyword.
'''
def myself(name,age):
    s1=f"Hi,My name is {name},and i'am {age} years old."
    print(s1)
myself('Roshan',22)
myself(age=21,name='Roshan')
'''
#5. Function parameter with default value(Optional Parameter)
"""
def multi(n1,n2,n3=1):
    return n1*n2*n3

ans=multi(2,3)
print("Multiplication=",ans)


    WAP to create a function with 3 optional parameters which
    display the multiplication of them?  

def multi(n1=1,n2=1,n3=1):
    return n1*n2*n3

ans=multi()
print("Multiplication=",ans)
print("Multiplication=",multi(23))
print("Multiplication=",multi(2,5))
print("Multiplication=",multi(2,3,4))

def value(num=5):
    for i in range(num):
        print(i,end=',')

print('Values with Arguments ')
value(3)
print('\nValues with Default Arguments')
value()

"""
#Keyword argument with optional parameters
"""
def show(name=None,age=18):
    print('Hii!',name,'Your age is',age)

show()
show('Rosh',22)
"""
#6. Variable Number of Arguments (*args)
''' 
    here we can pass any type values to function.
    It may be int,float,list,tuple i.e we can pass only single
    arguments.

    But with varible number arguments we can pass mutiple values in 
    arguments and it will store or print as a tuple format

'''
""" 
def printnumbers(nums):
    print(nums)
printnumbers(24)
printnumbers([25,34,54])

def printnumbers(*nums):
    print(nums)
printnumbers(24)
printnumbers(25,34,54)
printnumbers()
"""
#WAP to print addition of any n random numbers n number?
"""
def addition(*num):
    sum=0
    for i in num:
        sum=sum+i
    print('Addition=',sum)

addition(1,2,3,4)
addition(23,34,65)
'''
    If we want to pass iterable object like list,set etc to function
    we must pass with * symbol. 
'''
l1=[1,7,2,4]
addition(*l1)

'''
    Variable Number of Argument is also known as Python 
    Arbitary Non-keyword Argument.

    Sometimes,we dont't know in advance the number of arguments that will 
    be passed to the function.
    To handle this situation in python it allows us to define 
    a function using n number of varibale  arguments

    The parameter of the function prefix with *(asterisk)

    Syntax:
        def function_name(*args):
            statements

    The arguments which we pass to the function are wrapped into
    the tuple type.
    
    We can pass only the non keyword arguments to the function.
'''
"""
#Keyword Number of arguments
'''
    It is similar to the variable number of argument except 
    here we can pass value to function in keyword arguments form.

    The Keyword Number of arguments are prefix with the **(double astersik)
'''
"""
def userDetails(**kwargs):
    print(kwargs,type(kwargs))

userDetails(Id=101,name='Rosh',age=25)
"""
"""
emplist=[]
def addemp(**emp):
    emplist.append(emp)
    print('Employee is Added in list..')

print(emplist)
addemp(empid=101,empname='Roshan',empEmail='rosh@it.com')
addemp(empid=102,empname='Rohit',empEmail='rohit@it.com')
print(emplist)

''' If we want both of the arguments i.e Variable Number of Arguments &
Keyword Number of arguments we can use as follow:
'''
def function_name(*var1,**var2):
    pass
"""
def values(*num):
    print(num)

values(21,45,42)
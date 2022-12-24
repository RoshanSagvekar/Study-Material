# Exception Handling
'''
    What is Exception?
        Exception is abnormal condition which disturbs normal flow of program
        Excecution.

        Due to an exception program is terminated abnormally.

        Exception is also known as Error.

        Example:-
            Divide any number 0.
            10/0 --> infinity
                Python interpreter is not able execute above statement then
                it give an exception.
                i.e ZeroDivisionError

            l1=[3,5,67,86]
            print(l1[4])
                here we got the IndexError.
    There are 2 Types of error:-
        1.Runtime Error:-
            -This Error raiseduring the execution of program.
             And terminate program abnormally.
             but using exception handling we can handle them.

            Exception
                IndexError
                ZeroDivisionError
                ValueError
                KeyError
                FileNotFoundError
                etc.
            
        2.Syntax Error:-
            -This error raise before execution of program
            i.e at a time of program interpretation.
            So we can't handle these using Exception Handling.

            SyntaxError
            IndentationError
        
'''
"""
a=10/0
l1=[3,5,76,2]
print(l1[4])
print('Hi Python is Executing')
a=int('123a')
print(a)
if True:
"""

# What is Exception Handling?
'''
    Exception Handling is a mechanism in which we can handle 
    the Runtime Error and avoid abnormal termination of program.

    Because of Exception handling progrma execution will successfully completed
    with an error.

    To handle Exception in python we suppose to use some block or clause.

    1.Try block:-
        This is used to write the code which raise the exception during 
        execution.
        and theat exception/Error we easily except using except block.
    
    2.Except block:-
        This is used to write code which we want to execute after
        exception is raised in try block.
        (i.e it used to write handling code of error.
        like error messege printing act)
    
        try:
            Critical Statement
        except Error_class as obj:
            code to execute...

    3.Else block:-
        This block is used to define a statement which we want to execute 
        without exception.
'''
"""
a=int(input('Enter a Number1='))
b=int(input('Enter a Number2='))
try:
    div=a/b
    print('Try block completed.')
except ZeroDivisionError as e:
    print('Error is Occured in program.')
    print('Error:-.',e)
else:
    print('In program,Exception is not Raised.')
    print('Division',div)
print('Program completed')
"""

# Multiple Except block for single try block.
"""
try:
    a=int(input('Enter a Number1='))
    b=int(input('Enter a Number2='))
    div=a/b
    print('Try block completed.')
except ZeroDivisionError as e:
    print('Error is Occured in program.')
    print('Error:-.',e)
    print('2nd Entered number should not be 0.')
except ValueError as e:
    print('Error is Occured in program.')
    print('Error:-.',e)
    print('Please Enter only number.')
# It is used to handle each known exception separatly with proper message.
except Exception as e:
    print('Error is occured in program.')
    print('Error:-',e)
else:
    print('In program,Exception is not Raised.')
    print('Division',div)
print('Program completed')

"""
# Group of Exception in single except block.
'''
    It is used to handle some exception with common set of code.
'''
"""
try:
    a=int(input('Enter a Number1='))
    b=int(input('Enter a Number2='))
    div=a/b
    print('Try block completed.')
except(ZeroDivisionError,ValueError) as e:
    print('Error is occured in program.')
    print("Error:-",e)
    print('!!!...PLEASE ENTER VALID INPUTS...!!!')
except Exception as e:
    print('Error is occured in program.')
    print("Error:-",e)
else:
    print('In program,Exception is not Raised.')
    print('Division',div)
print('Program completed')
"""
# Finally block
'''
    4.Finally block
        It will always execute with or without exception.

        Finally block can be define after try block as well as 
        except block also.
'''
"""
l1=[2,4,45,46,6]
try:
    index=int(input('Enter the index to print its value:'))
    value=l1[index]
except IndexError as e:
    print('Error:-',e)
    print('Please enter valid index for list.')
else:
    print("Value is",value)
finally:
    print('I am Finally block')
"""

# Raising Exception
'''
    In python,
        Exceptions are raised automatically during execution of 
        Critical Statement.

    If we want to raised an exception manually(Explicitly) in python,
    we use "Raise" keyword.

    5.Raise Keyword
        -it is used to raised the exception manually.
        -it helps the developer to raise the exception with custom 
          message.
'''
"""
try:
    a=int(input('Enter a Number1='))
    b=int(input('Enter a Number2='))
    if b==0:
        #errorobj=ZeroDivisionError('n2 should not be 0')
        #raise errorobj
        raise ZeroDivisionError('n2 should not be 0')
    div=a/b
except ZeroDivisionError as e:
    print("Error:-",e)
else:
    print("Division=",div)
"""

#Custom Exception / User Define
"""
class AgeError(Exception):
    pass

def isvalidAge(age):
    if age<18:
        raise AgeError('Your age is less than 18.')

try:
    age=int(input('Enter your age='))
    isvalidAge(age)
except AgeError as e:
    print("Error:-",e)
else:
    print('You are eligible for vote.')
"""
"""
class MobileNoError(Exception):
    pass

def isValidMobileNo(num):
    if len(str(num))!=10:
        raise MobileNoError('Your Mobile number is Invalid. ')

try:
    mno=int(input('Enter your Mobile Number='))
    isValidMobileNo(mno)
except MobileNoError as e:
    print("Error:-",e)
else:
    print('Your Mobile Number:-',mno)
"""

# Assert keyword
'''
    In Python assert keyword statement used to debug the python program.
    Syntax:
        assert condition,Error_messeage:

    here assert statement execute program continuosly if the condition
    is True otherwise it raise the assert exception with specified msg.
'''
"""
a=3
print('Statement-1')
print('Statement-2')
assert a%2==0,'Number is not even' 
print('Statement-3')
print('Statement-4')

"""
# Write a program to validate Mobile Number length using user define exception (input in int type only)
"""
class MobileNoError(Exception):
    pass

def isValidMobileNo(num):
    if len(str(num))!=10:
        raise MobileNoError('Your Mobile number is Invalid. ')

try:
    mno=int(input('Enter your Mobile Number='))
    isValidMobileNo(mno)
except MobileNoError as e:
    print("Error:-",e)
else:
    print('Your Mobile Number:-',mno)
"""

# Write a program to explain else statement proper comments with notes 
"""
a=int(input('Enter a Number1='))
b=int(input('Enter a Number2='))
try:
    div=a/b
    print('Try block completed.')
except ZeroDivisionError as e:
    print('Error is Occured in program.')
    print('Error:-.',e)
# it is used to define a statement which we want to execute without exception.
else:
    print('In program,Exception is not Raised.')
    print('Division',div)
print('Program completed')
"""
# Write a program to explain raise keyword proper comments with notes.
"""
try:
    a=int(input('Enter a Number1='))
    b=int(input('Enter a Number2='))
    if b==0:
        # raise keyword is used to raised exception manually.
        raise ZeroDivisionError('Number2 should not be 0')
    div=a/b
except ZeroDivisionError as e:
    print("Error:-",e)
else:
    print("Division=",div)
"""
# Write a program to multiple except in one try with proper comments and notes.
"""
try:
    a=int(input('Enter a Number1='))
    b=int(input('Enter a Number2='))
    div=a/b
    print('Try block completed.')
except(ZeroDivisionError,ValueError) as e:
    print('Error is occured in program.')
    print("Error:-",e)
    print('!!!...PLEASE ENTER VALID INPUTS...!!!')
except Exception as e:
    print('Error is occured in program.')
    print("Error:-",e)
else:
    print('In program,Exception is not Raised.')
    print('Division:',div)
print('Program completed')
"""




























#What is Lambda Function
'''
    The function which is define without a name known as 
    Lambda function.

    Lambda function is also known as Anonymous function.

    Lambda function is shorter syntax to define function in python.

    In normal function we use def keyword to define function
    but in lambda we use lambda keyword to define a function

    Syntax:-
        Variable_name=lambda (parameters):Statements

    Note:-lamda function can contain any number of parameters 
    but only one statement as body. 

    we need lambda function in variable.
'''
#Example1 (Normal Function) 
"""
def hello():
    return'Hi Everyone,\n\tGood Evening'
print(hello())
"""
#Lambda Expression
"""
welcome=lambda:"Welcome To Python Programming."
print(welcome())
"""
#lambda function with parameter

sq=lambda n:n**2
n=int(input('Enter a number='))
print('Square of',n,'is',sq(n))

add=lambda a,b:a+b
print('Addition of 3 and 4 is',add(3,4))

#Python Function as Parameter/Argument
'''
    The below function contains 3 parameter
    1st parameter as fucntion.
    Other 2 parameter are numbers.
'''

def calcy(action,a,b):
    return action(a,b)
print("Addition=",calcy(add,2,3))

print("Multiplition=",calcy(lambda a,b:a*b,2,3))
print("Subtraction=",calcy(lambda a,b:a-b,45,5))
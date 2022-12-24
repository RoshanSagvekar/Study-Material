'''
    There are 2 types of variable
    1.Global Varibale
        The varible which is declare inside python file(python module)
        and outside any functin is known as global variable.

        Scope of these type is on complete file or programs.
        i.e we can access this variable into any function also.
    
    2.Local Variable
        Tha variable those are declare inside function is known as 
        local variable.

        Scope of this variable within function.

'''
"""
num=25
def test():
    num=36  #If we assign a value to global variable in any function
            #Python interpreter will create new local variable with same name.
    print('Within Function Num:-',num)

test()
print('Outside Function Num:-',num)
"""
#Accessing Global Variable inside Function

num1=5
def test2():
    global num1      #It is used to access global in local scope.
    num1=6
    print('Within Function Num1:-',num1)

test2()
print('Outside Function Num1:-',num1)


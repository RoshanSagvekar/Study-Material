'''
Explain the following methods in maths module with an example
    -math.sqrt(x)
        Return the square root of x.

    -math.pow(x,y)
        Returns the x raised to y power.
        raises value error if x not integer or is negative value

    -math.factorial(x)
        Returns the factorial of x.

    -math.floor(x)
        Returns the floor of x,the largest integer less than or equal to x.
        if xis not float it will return as it is.

    -math.ceil(x)
        Return the ceiling of x, the smallest integer greater than or equal to x.

    -math.pi
        Returns the constant value of pi i.e 3.14
''' 
import math
print('Square root of',144,':',math.sqrt(144))
print('3rd power of 5:',math.pow(5,3))
print('Factorial of 5:',math.factorial(5))
print('Floor Value of 3.245:',math.floor(3.245))
print('Ceil Value of 3.245:',math.ceil(3.245))
print('Value of Pi:-',math.pi)
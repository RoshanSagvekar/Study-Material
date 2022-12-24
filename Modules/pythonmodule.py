#What is module?
'''
    Module is nothing but python file(.py)
    module is refer to a python file (.py) which python statements.
    like variable (global) Declaration,function definition and
    class definition.
    E.g
        example.py
            It is module of the python.
'''
#Current Executing python file is known __main__ module.
print("Name of current module is",__name__)

#Why we need module?
'''
    It is used to achieve modular programming in python.
    which helps the developer to breakdown large program in small
    piece of code.
    which easy to manage and organize the python code.

    It also provide the reusability,so we can define a most used
    function in a specific module and import that module anywhere as per need.
'''
#Types of Python Module.
'''
    There are 2 types of modules.
    -> Built in Modules(System defien module)
    -> Custom Module (Developer/Programmer define module.)
'''
#Built-in Module
'''
1.Core Module(No need to install)
    Python has huge set library which provide list module 
    and function to perform specific.

    Some module of python are already install with pyhton install
    which core module of python.

    like math,datetime,sys,os etc.

2.External Python Library(Need to install before use):-

    Web developement related library must be install before use.
        flask,django
    Database related Library
        pymysql,mysqlclient etc
    Data Science
        numpy,pandas,matplotlib etc.

    #How To install these library

    python -m pip install library_name

    e.g
        python -m pip install flask
            pip-->Python package index(python installer)
            which install the python packages and module.
'''
"""
import sys
print(*sys.path,sep="\n")
print("Type of sys.path is",type(sys.path))
"""
# Different way To import module.
# Math module
"""
import math
print('Square of 2:-',math.sqrt(2))
print('type of sqrt',type(math.sqrt))
print('Value pi:-',math.pi,type(math.pi))
"""
# We can access function and variable of module by 
# module_name.functio_name or module_name.variable

#Rename the python module after import
#import module_name as new_name
"""
import math as m
print('Square of 2:-',m.sqrt(2))
print('Value of Pi:-',m.pi)
"""

#Access the function or variable of module diectly
"""
from math import pi,sqrt,floor
print('Pi:-',pi)
print('Sqaure root of 144:-',sqrt(144))
print('Floor of 3.14:-',floor(3.14))
"""
"""
import datetime as dt
today=dt.datetime.now()
print('Today:-',today)
today=dt.date.today()
print('Today:-',today)
"""

#Custom Modules
'''
    Module file has in same directory 
'''
#Custom module in same directory
"""
import mymodule
mymodule.sayhi()
"""
#Configuration of modules when present in different location
"""
import sys
sys.path.append(r'F:\Python\pythonlib')
#It contains the path

import testmodule as ts
print(ts.sayWelcome())
"""
#Package 
'''
    Package is a directory(folder) which contains the 
    list of python module(files).

    One Package can contain a another sub package also.

    It help you create a your own heirarchy of module
    for a single pythn application.

    Every python package contains a one default module which 
    is known as __init__.

    __init__ module will help initialize python package.
'''

#here we import package
import pythonstmt as ps
#namespace full qualified name module
#import pythonstm.conditionalstmt.pycs
#pycs.isEvenorOdd(32)
ps.isEvenorOdd(32)
ps.table(3)
#String
'''
    What is String?
        String is collection of characters.

    How to create a object of string in python?
        There are 3 ways to create an object of string in python.
        1.Using single quote
            Enclosed a set of character into single quotes.
            e.g
                str='Hello'

        2.Using Double quotes
            Enclosed a set of character into double quotes.
            e.g
                str="Rajesh"
        3.Using triple quote of single or double quoted
            Triple quotes of single or double quotes creates 
            a multiple line of string in python.
            e.g
                s1="""......"""
'''
#Single quotes
s1='Raj'
'''print('s1:-',s1)'''
#Double quotes
s2="'Rajesh'"
'''print('s2:-',s2)'''

#In other language
#'C'  ->Char type
# "C" ->String Type
#Char datatype is not supported in python.

#Triple quote
s3='''Hi,This is python string demo.
    We are learning string creation way.'''

s4="""Hi,This is python string demo.
    We are learning string creation way."""
'''
print(s3)
print(s4)
'''
#String is immutable datatype of python.
s1='raj'
s2="raj"
'''
print(s1,id(s1))
print(s2,id(s2))
'''
#String allows index to access the character of string.
# the index of string is start from 0
s1='ITVedant'
'''print('s1[0]',s1[0])
print('s1[2]',s1[2])'''
#It allow the negative index to access the character like list.
#Negative index start from -length to -1

#Slicing with String
'''
    Slicing used to create substring in python.

    strobject[startindex:endindex:step]
        here
            default value is step 1
                    then start=0 & endindex=length
            if step is -1 or negative
                Slicing will be start from last index


s2=s1[:]
print('s2:',s2)
s2=s1[2:]
print('s2:',s2)
s2=s1[2:5]
print('s2:',s2)
s2=s1[1::2]
print('s2:',s2)
s2=s1[::-1]
print('s2:',s2)
s2=s1[6:2:-1]
print('s2:',s2)
'''
#METHOD OF STRING CLASS
# str() function
'''It is used to achieve type casting into string type.

i=123
s1=str(i)
print(i,type(i))
print(s1,type(s1))
'''

#Methods:-
"""
# # 1.Capitalize()
#   It is used to convert the first character of string into uppercase.
 
s1='hi,this is Roshan Sagvekar.'
print(s1.capitalize())
#
print(s1.upper())
#
print(s1.lower())
#title converts the 1st character of each word to upper case
print(s1.title())
print(s1.swapcase())

s2='  Hello  '
print('s2:-',s2,'Length=',len(s2))
s3=s2.strip()       
print('s3:-',s3,'Length=',len(s3))
s4=s2.lstrip()
print('s4:-',s4,'Length=',len(s4))
s5=s2.rstrip()
print('s5:-',s5,'Length=',len(s5))

"""

#split():-
"""
s1='''Hi,Everyone,
Welcome to String handling demo
This split method Example
'''

l1=s1.split('to')
print(l1,len(l1))
l1=s1.split(' ',5)
print(l1,len(l1))

l2=s1.splitlines()
print(l2,len(l2))
"""
#Join
"""
s1=','
l1=['Raj','Rohan','Rohit','Suraj','Priya']
s2=s1.join(l1)
s3='-'.join(l1)
print('Joined String:-',s2)
print('Joined String:-',s3)
"""
#Startwith()
"""
s1='ITvedant'
print('is String start with IT',s1.startswith('IT'))
if s1.startswith('IT'):
    print('Yes..Start with IT')
else:
    print('No..Start with IT')
"""
#Endswith()
"""
s2='ITvedant'
print('is String ends with ant',s1.endswith('ant'))
if s2.endswith('ant'):
    print('Yes..end with ant')
else:
    print('No..end with IT')
"""
# default Format Method
"""
str1='Hi,\n\t I am {},and i am {} years old.'
# here curly braces are used to create placeholder.
s1=str1.format('Raj',22)
print(s1)
"""
#Format method with index.
"""
str1='Hi,\n\t I am {1},and i am {0} years old.'
s1=str1.format(22,'Rohit')
print(s1)
"""
#Format method with index.
"""
str1='Hi,\n\t I am {name},and i am {age} years old.'
s1=str1.format(name='Ram',age=23)
print(s1)

n=input('Enter name=')
a=input('Enter age=')
str1='Hi,\n\t I am {name},and i am {age} years old.'
s1=str1.format(name=n,age=a)
print(s1)
"""

#Type of String in Python
#1. Plain String
s1="Good Evening\n\tHi,Rosh"
print(s1)

#2. Raw String
#Raw String is prefix with the r letter & used to repersent string as it is.
s2=r"Good Evening\n\tHi,Rosh"
print(s2,type(s2))
s3=r'E:\python\test.txt'
print(s3,type(s3))

#3. Formatted String
name='Raj'
s4=f"Good Evening!\n\tHi,{name}"
print(s4,type(s4))

#4. Byte String
name='Roshan'
s5=b"Good Evening!\n\tHi,{name}"
print(s5,type(s5))


# File Handling
'''
    File Handling is one of the most importatnt mechanism of python in which 
    we can perform file operation like create,open,read,write,delete etc in file 
    hard disk.

    All the operation we can perform of file using file.
    And File object is created using
    open(function)

    Syntax:-
    my_file=open(filepath,filetypeandmode)

    File Type:
        There are 2 types of file type
        1.text file denoted by t (Default Type)
        2.Binary file denoted by b
    File Mode:-
        There are 4 type of File Mode.

        1. x :-
            It used to create New File always.
            if file is already exists then it give Error.

        2. r :-(default)
            It is used to open a file in read only mode.
            in this mode if file is not exists gives error.
            It is default file mode.

        3. w :-
            It is used to open a file in write only mode.
            If file is exist then it will overrwrite.
            if file is not then it will creaate in specified dir.

        4. a :-
            It is also used to open file in append mode.
            It never overwrite the content of existing file.

        5. r+   Read and Write
        6. w+   Write and Read
        7. a+   Append and Read

'''

import os
from sys import path
from typing import final
print("Current:-",os.getcwd())
#print("File of CWD",os.listdir())

# # X- writeonly mode with new file always
"""
my_file=open('test.txt','tx')
my_file=open('test.txt','t')
"""
# read only mode
"""
my_file=open('test.txt','tr')
#my_file.write('hi')
print(my_file.read())

my_file=open('test.txt','tr')
#my_file.write('hi') Can't write the data into file(it is open in readonly mode)
print(my_file.read())

"""
# writeonly mode
"""
my_file=open('test.txt','w')
my_file.write('Hii')
my_file.close()
"""
#Append only mode
"""
my_file=open('test.txt','a')
my_file.write('Hii')
my_file.close()
"""

# Method
# tell():- it is used to find current position of file.
# seek():It is used to change current position file 
# to specified position.

"""
try:
    my_file=open('test.txt')
    data=my_file.read(6)     # read specified No. of character.
    print(data)
    print('Current Position:-',my_file.tell())
    data=my_file.read(14)   # read specified No. of character.
    print('Current Position:-',my_file.tell())
    print(data)
    my_file.seek(10) # here we set the current position is 
    print('Current Position :- ',my_file.tell())
    data = my_file.read(5)  
except Exception as e:
    print('Error',e)
finally:
    my_file.close()
    print('File is closed successfully.')

"""
# Read a single Line from file
"""
try:
    my_file=open('test.txt')
    line=my_file.readline()
    print(line)
    line=my_file.readline()
    print(line)
except Exception as e:
    print('Error',e)
finally:
    my_file.close()
    print('File is closed successfully.')
"""
# Read All Lines from file.
"""
try:
    my_file= open('test.txt')
    #lines = my_file.readlines() # read a All lines from file.(return list of line)
    #print(lines)
    for line in my_file.readlines():
        print(line,end='')
except Exception as e:
    print('Error ',e)
finally:
    my_file.close()
    print('\nFile is Closed Successfully.')
"""
# r+ read and write mode.
"""
try:
    my_file= open('test.txt','r+')
    data=my_file.read()
    print(data)
    s1="This is a new data of my file"
    my_file.write(s1)
except Exception as e:
    print('Error ',e)
finally:
    my_file.close()
    print('\nFile is Closed Successfully.')
"""
# w+ write and read mode
"""
try:
    my_file= open('test.txt','w+')
    data=my_file.read()
    print(data)
    s1="\nThis is a new data of my file"
    my_file.write(s1)
except Exception as e:
    print('Error ',e)
finally:
    my_file.close()
    print('\nFile is Closed Successfully.')

# In this we are reading new data from file that is overwrite.

try:
    my_file= open('test.txt','w+')
    my_file.write('This Write only mode with read.')
    print('Current Position:-',my_file.tell())
    my_file.seek(0)
    data=my_file.read()
    print(data)
except Exception as e:
    print('Error ',e)
finally:
    my_file.close()
    print('File is Closed Successfully.')
"""
# Open file in Writeonly mode only.
"""
try:
    my_file= open('test.txt','w')
    my_file.write('This Write only mode')
    my_file.read()This Write only mode
except Exception as e:
    print('Error ',e)
finally:
    my_file.close()
    print('File is Closed Successfully.')
"""

# Open file in write only mode without overwritting.
"""
try:
    my_file= open('test.txt','a')
    my_file.write('\nThis Write only mode without Overwriting(i.e append mode')
    my_file.read()
except Exception as e:
    print('Error ',e)
finally:
    my_file.close()
    print('File is Closed Successfully.')
"""
# a+
"""
try:
    my_file= open('test.txt','a+')
    my_file.write('\nThis Write only mode without Overwriting(i.e append mode')
    my_file.read()
except Exception as e:
    print('Error ',e)
finally:
    my_file.close()
    print('File is Closed Successfully.')

"""
# Binary Mode
# bw
'''
try:
    file_bin=open('test2.bin','bw')
    s1=b"Hi,This is Binary String"
    file_bin.write(s1)
except Exception as e:
    print('Error',e)
finally:
    file_bin.close()
    print('File is closed Successfully.')
'''
# br
"""
try:
    file_bin=open('test2.bin','br')
    data=file_bin.read()
    print(data)
except Exception as e:
    print('Error',e)
finally:
    file_bin.close()
    print('File is closed Successfully.')
"""

# image file
path=r'E:\sign.jpg'
try:
    file_bin = open(path,'br')
    data = file_bin.read()
    #print(data)
    
    #file 2:
    file_bin2 = open('v.png','bw')
    file_bin2.write(data)
    
except Exception as e:
    print('Error ',e)
finally:
    file_bin.close()
    file_bin2.close()
    print('File is Closed Successfully.')
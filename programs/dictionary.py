#Dictionary
'''
    Dictionary is one of the python datatype.
    It is used to hold the data in form of pair which contain 
    key and value.
    It is changeable.
    Keys of dictionary is unique as well as it is immutable type of data.
    Value can be duplicate also or any type(mutable and immutable)

    If we insert/add a duplicate key,python will update the value
    of existing with a new value.

    Dictionary is created in python by using curly braces i.e { }

    Syntax:-
        variable_name={}
        variable_name={key:value,......}

'''
#E.g 
'''
d1={}   #(Empty Dictionary)
#{} o/p
print(d1)
d1['empid']=101
d1['empName']=102
print('Dictionary-1:-',d1)
#Dictionary-1:- {'empid': 101, 'empName': 102}  o/p
d2={'sid':1001,'sname':'Roshan'}
print('Dictionary-2:-',d2)
#Dictionary-2:- {'sid': 1001, 'sname': 'Roshan'}       o/p

d1['empid']=102
print(d1)
'''

emp={
    'empId':101,
    'empName':'Raj',
    'empsalary':15000
}

#Access the value of dictionary.
'''Dictionary don't have any index to access it values.
we can take key as index to access its values.'''

print('Employee Name:-',emp['empName'])
print('Employee Salary:-',emp['empsalary'])

#Get values of any key of dictionary by method.
'''
    1.get(key)
        return values of specified key as argument.
'''
print('Employee Name:-',emp.get('empName'))

#get all the keys of dictionary.
'''
    2.keys()
        return the list of all the keys preent in dictionary.
'''
print('keys:-',emp.keys())

#get all the value of dictionary.
'''
    3.values()
        return the list of all the values print in dictionary.
'''
print('Values:-',emp.values())


#get all the pairs(key,values) of dictionary.
'''
    4.items()
        returns the list of tuple which contains the key and values.
''' 
print('Key and Values:-',emp.items())

items=emp.items()
for key,value in items:
    print(key,value,sep=' : ')

#WAP to print key and value of dictionary without using items()?
emp={
    'empId':101,
    'empName':'Raj',
    'empsalary':15000
}

for i in emp.keys():
    print(i,':',emp[i])

for key in emp:
    print(key,':',emp[key])


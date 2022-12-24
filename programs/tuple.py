#Tuple
'''
    ->Tuple is one of the sequence datatype of python.

    ->Tuple allowed to store a multiple value of any type in 
        a single variable.

    ->Tuple is created using round brackets().

    ->Tuple also the indexes to access its element.

    ->It is collection of fix value.
    ->It is also known as immutable datatype(values of tuple 
        can' be change.),

    ->Tuple allows dulicate elements.

'''
'''
t1=(12,36,74,96,74)
print(t1)
print('t1[0]:-',t1[0])
print('t1[2]:-',t1[2])
'''
#t1[1]=46   can't change value on any exisiting tuple.

t1=(1,3)
t2=(1,3)
print(t1,"Address of t1",id(t1))
print(t2,"Address of t2",id(t2))

for elements in t1:
    print(elements,end=',')

#Methods of Tuple
'''
    index(element,start,end):-Return the index of 1st occurence of specified element .
    count(element):-return the count of specified element.
'''
t1=(1,54,23,64,6,24,23,1)
print('Index of 23:-',t1.index(23))
print('Count of 23:-',t1.count(23))

#Nested Calling
print('Index of 2nd occurence ')
#Built In Function
"""
#max(iterable)
l1=[23,5,7,4,8,3,8,2]
print('Maximum Value in l1:-',max(l1))
#min(iterable)
print('Minimum Value in l1:-',min(l1))
#sum(iterable)
print('Sum of all Value in l1:-',sum(l1))
"""

#Filter
'''
    This filter function contains 2 parameters
    filter(function,iterable)
    This function is used to filter any existing iterable and return
    the filter object.
'''
l2=[4,6,8,3,8,4,9,3]

#Filter only even no from l2.
"""
def isEven(n):
    return n%2==0

filterobj=filter(isEven,l2)
evenlist=list(filterobj)
print('Even numbers in l2:-',evenlist)
"""
#Filter only odd no from l2 with lamda function.
"""
oddlist=list(filter(lambda n:n%2==1,l2))
print('Even numbers in l2:-',oddlist)
"""
#Note :- Pass only condition based function to the filter function as a arguments.

#map()
'''
    map(function,iterable):-
        This function returns the map object of the result after applying
        the given function to each item/element of given iterable.
'''
"""
l1=[4,7,6,3,8,3,8]
sqlist=list(map(lambda n:n**2,l1))
cubelist=list(map(lambda n:n**3,l1))
print('List1:-',l1)
print('Square List of List1=',sqlist)
print('Cube List of List1=',cubelist)
"""
#zip()
'''
    This function take n number of iterable arguments 
    and return map object which contains the iterator which contains the element of 
    each iterable of same index.
'''
""" 
ziplist=list(zip(l1,sqlist,cubelist))
print(ziplist)
"""
#If list has different number of elements.
"""
l1=[1,2,3,4,5]
l2=[4,3,6,2]
ziplist1=list(zip(l1,l2))
print(ziplist1)

userlist=[[101,102,103],['Raj','Jay','Ram'],[25,24,23]]
userziplist=list(zip(*userlist))   #here * is used to access all the inner list.
print("User Zip List:",userziplist)
""" 

#reduce
'''
    reduce(function,iterable)
        This function is used to reduce the iterable object 
    as arguments with specified functionality.

    Argument function of reduce contains 2 parameters.

    This reduce function is present in functools module.
    so before call this function we have to import that module 
    in current.


''' 

from functools import reduce    #we import a function from module.
l1=[2,1,7,3,8]

ans=reduce(lambda a,b:a+b,l1)
print('Sum of l1 elements:-',ans)
ans=reduce(lambda a,b:a*b,l1)
print('Multiplication of l1 elements:-',ans)


a='A'
print(ascii(a))
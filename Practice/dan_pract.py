# How to sort a Python dict by value
# (== get a representation sorted by value )

'''xs ={ 'a':4,'b':3,'c':2,'d':1 }
print(sorted(xs.items(), key=lambda x: x[1]))
'''
# OR

'''import operator
print(sorted(xs.items(),key= operator.itemgetter(1)))'''



# How to merge two dictionaries

'''x = {'a':1,'b':2}
y = {'c':3,'d':4}
z={**x,**y}
print(z)'''


# Different ways to test multiple flags at once
'''x, y, z = 0, 1, 0
if x == 1 or y == 1 or z == 1:
    print('passed')

if 1 in (x, y, z):
    print('passed')'''

# These only test the truthness:
'''if x or y or z:
    print('passed')

if any((x,y,z)):
    print('passed')'''
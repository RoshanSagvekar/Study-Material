#Frozen set
'''
    Frozen set is an immutable version of python set.
    Duplicate not allowed.
    can't accessed by index.
    Unordered.
    Fixed set.

    The main difference of set and frozen set is that 
    set values can be modify by method like add,pop,remove,
    discard where as frozenset can't be modify.

    Syntax:
            variable_name=frozenset()
            variable_name=frozenset(iterable)

            itrable is also known as sequence datatype.
'''
#E.g
fset=frozenset()
print('Empty Frozen set:-',fset)
t1=(1,3,43,54,2,3)
fset1=frozenset(t1)
print('Frozen set:-',fset1,type(fset1))
'''
for i in fset1:
    print(i,end=',')
'''
#fset1.add(25)
fset2=frozenset((36,41,2,1,3))
s1=fset1.difference(fset2)
print("fset1:-",fset1)
print("fset2:-",fset2)
print("s1:-",s1)


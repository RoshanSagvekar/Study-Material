#Set
'''
    ->Set is also python data which allows us to store
    multiple values in single variable.
    Syntax:-
        variable_name={values seperted by comma}

    ->Set allows only the unique values.
        It does not allows duplicate values.
    
    ->Set is an Unordered.
    ->Set does not allow indexing to access the element of it.

    ->Set can store only immutable type values only.

    ->We can not create empty set using {}.
        because blank { } are defined as a Dictionary.
    
    ->To create empty set in python we suppose to use set function.
'''
'''
s1={13,56,87,2,3,56,(12,6),'Str'}
print(s1)

l1=[]
print(type(l1))
t1=()
print(type(t1))
s1={}
print(type(s1))
s1=set()
print(type(s1))
'''

#Methods Of Set
'''
    1.Add(element):-
        It is used to add the element in existing set.
    2.Update():-
        It is used to add the multiple values of any other sequences.
    3.pop():-
        It remove element from set and return it.
    4.discard(element):-
        It is used to remove the specified element from set.
        It will not throw a error if specified element does not found.
    5.remove(element):-
        It is used to remove the specified element from set.
        It will throw a error(key error) if specified element does not found.



s1={13,54,3,12}
print('s1:-',s1)
s1.add(36)
print('After Add\ns1:-',s1)
s1.update([12,64,96])
print('After Update\ns1:-',s1)
ele=s1.pop()
print('After Pop\ns1:-',s1)
print('Removed Element=',ele)
ele=s1.discard(13)
print('After Discard\ns1:-',s1)
print('Removed Element=',ele)
ele=s1.remove(12)
print('After Discard\ns1:-',s1)
print('Removed Element=',ele)
'''
#Union and Intersection
'''
    6.Union():-
        ->Create union of 2 different set.
        ->returns all the values from both set and commons values returns only once.

    7.Intersection():-
        ->return the common values of both set.

'''
s1={1,26,1,5,74}
s2={2,26,56,5,41}

#print('Union of s1 & s2:-',s1.union(s2))
#print('Intersectionof s1 & s2:-',s1.intersection(s2))
'''
s3=s1.union(s2)
s4=s1|s2
print('Union of s1 & s2:-',s3)
print('Union of s1 & s2:-',s3)

s3=s1.intersection(s2)
s4=s1&s2
print('Intersectionof s1 & s2:-',s3)
print('Intersectionof s1 & s2:-',s4)
'''
#Difference
'''
    It used to subtract 2 set and returns set which contain
    uncommon values of 1st.


s1={1,26,11,5,74}
s2={2,26,56,5,41}
s3=s1.difference(s2)    #return un-common values of set 
s4=s1-s2
print('s1:-',s1)
print('s2:-',s2)
print('Difference (method):-',s3)
print('Difference (operator):-',s4)
'''

#Symmetric_difference()
'''
    This method return set of un-common values of both set
'''
'''
s1={1,26,11,5,74}
s2={2,26,56,5,41}
s3=s1.symmetric_difference(s2)    
s4=s1^s2        #^ is Symmetric differece operator.
print('s1:-',s1)
print('s2:-',s2)
print('Difference (method):-',s3)
print('Difference (operator):-',s4)
'''

'''
    As you all knows above methods of set are performing specific
    operation on set like union,intersection etc.
    But not even single method is modified any existing set on
    which method is called.

    If we want to modify existing with resultant set,we can us following method.
    -> 1.intersection_update()  &
    -> 2.difference_update()    -
    -> 3.symmetric_difference_update()  ^

'''
s1={1,26,11,5,74}
s2={2,26,56,5,41}
#s1.intersection_update(s2)
'''
s1&=s2
print('s1:-',s1)
print('s2:-',s2)

s1.difference_update(s2)
s1-=s2
print('s1:-',s1)
print('s2:-',s2)

s1.symmetric_difference_update(s2)
s1^=s2
print('s1:-',s1)
print('s2:-',s2)
'''
#WAP to create set 1 to 20 numbers.
'''
s1=set(range(1,21))
print(s1)
'''
#WAP to create set 1 to 20 numbers those are divisible by 3 & 5.
'''
s1=set()
for i in range(1,21):
    if(i%3==0 and i%5==0):
        s1.add(i)
print(s1)
'''
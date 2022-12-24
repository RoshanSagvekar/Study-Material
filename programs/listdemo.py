#Datatype:-int,float,bool,complex(All these will store a single value in variable at a time)
#Sequence datatype:-List,Tuple,Set,frozen set,dictionary,string.

#List:-
'''
    ->List is one of the datatype of python which allows us to store
multiple value of any type in a single variable.

    ->Values of the list are called as elements/items.

    ->List is created using square brackets[value,]

    ->It allows the index to access the value from list.
    ->list index are start from 0.

    ->List allows the duplicate values.
    ->List is ordered(follow the insertion order)
    ->It is mutable datatype i.e the value of list can be changed at run time.

#e.g
l1=[1,25,23,14]
l2=[1,1.1,True,3+2j,[12,11,13],(1,32),{12,43},'String']
print('1st value of l1:-',l1[0])
print('5t value of l2:-',l2[4])
print(l1)
print(l2)
l1[0]=25
print(l1)
'''

#List Function
'''
l1=range(1,10)
print('l1:-',l1)
print('Type of l1:-',type(l1))

#list is built-in-function which convert any compatible sequence type in list.
l2=list(range(1,10))
print('l2:-',l2)
print('Type of l2:-',type(l2))

s2='Roshan'
l3=list(s2)
print('l3:-',l3)
print('Type of l3:-',type(l3))

'''
#Methods of List datatype.
'''
1.append(element):-
    It is used to add new single element in list.
    e.g l1.append(45)
        l1.append('Rosh')

2.extend(seuence obj):-
    It is used to add multiple element in list(any other sequence)
    e.g l1.extend([45,78,'Ash'])

3.insert(index,element):-
    It is also used to add single element into list at specific position.
    E.g  l1.insert(1,35)

4.pop(index)
    It is used to remove the value by the index.
    it will return the value which remove.

    pop()
        It will remove the value by right hand side.

5.remove(element)
    It is used to remove specified element from the list.

6.clear()
    It is used to remove all the element of the list.
'''
'''
l1=[]
print('l1:-',l1)

l1.append(45)
l1.append('Rosh')
l1.append(29)
print('After Append')
print('l1:-',l1)

l1.extend([45,78,'Ash'])
print('After Extend')
print('l1:-',l1)

l1.insert(1,35)
print('After Insert')
print('l1:-',l1)

element=l1.pop(2)
print('\nAfter pop:-',l1)
print('Removed Element is:',element)

element=l1.remove(29)
print('After Remove:-',l1)
print('Removed Element is:',element)

element=l1.clear()
print('After Clear:-',l1)
'''
'''
   8. copy():-
        It returns a shallow copy of the list

l1=[12,3,43,3,25]
#l2=l1    (it is deep copy)      #-->here it will copy the address of variable.
l2=l1.copy()    #It is shallow copy --->here it will copy the elements of variable.
print('l1:-',l1,'Address',id(l1))
print('l2:-',l2,'Address',id(l2))
l1.remove(3)
print('l1:-',l1)
print('l2:-',l2)
'''

'''
    9.count(element):-
        returns count of element which is specified into argument.

    10.index(element)
        return the index of the first matched element,
    it will start to search the element from 0th index.

    11.index(element,startindex,end)
        return the index of the first matched element,
    it will start to search the element from specified index.

    12.sort(reverse=False)
        It will sort the element of list in ascending order.
    
        sort(reverse=True)
        It will sort the element of list in descending order.

l1=[25,96,74,87,74,25,41,25,74]
print('Count of 25=',l1.count(25))
print('1st index of 74 is',l1.index(74))
print('1st index of 74 is',l1.index(74,3))
print('Before Sort',l1)
l1.sort(reverse=True)
print('Before Sort',l1)
'''
#Nested List
'''
l2=[(101,'Raj'),(104,'Rosh'),(102,'Rohit'),(103,'Priya'),(105,'Ashish')]
'''
#User Defined function
'''
def secondvalue(element):
    return element[1]   #returns the index of inner datatypes

print(secondvalue(l2))

for element in l2:
    print(secondvalue(element))
'''
#Sorting on the nested list
'''
l2.sort()
print('After Sort(default sort)',l2)
l2.sort(key=secondvalue)
print('After Sort(',l2)
'''

'''
    13.reverse()
        reverse the order of item.

l1=[34,76,8,3,87,12]
print('l1:-',l1)
l1.reverse()
print('l1:-',l1)
'''

#H.W

l2=[(101,'Jay',85.96),(102,'Raj',66.14),
    (103,'Amit',77.74),(104,'Priya',47.96)]

#WAP to sort above list on the basis of student percentage
def per(element):
    return element[2]
l2.sort(key=per)
print('Sorted list according to percentage:\n',l2)

'''
#WAP to accept the element from user and count its occurrences into
#given list.

l1=[1,2,3,4,5,6,3,2,5,2,5,5,7,3,6,8]
n=int(input('Enter a number='))
print('Count of',n,'=',l1.count(n))
'''

#As you all know list allows indexing to access the element.
# ->Positive index
# ->Negative index
l1=[12, 6, 16, 19, 34, 6, 5]
#   0   1   2   3   4  5  6       positive indexing
#   -7 -6  -5  -4  -3 -2 -1       Negative indexing
'''
print('l1[1]:-',l1[1])
print('l1[1]:-',l1[-1])     #Returns last value of l1.
''' 
#Reverse List
'''
for index in range(-1,-7,-1):
    print(l1[index],end=',')
'''

#Slicing
'''
    ->Slicing is used to create a sub list.
    ->It help to split list in sub part.
    ->Syntax:-
            listvariable[startindex:endindex:step]

            here endindex element is not included in sublist.

    ->negative step is used to read the element in negative order.
'''
'''
print(l1[:])
print(l1[2:4])
print(l1[::2])
print(l1[2:-1])
print(l1[-2:-5:-1])
#Create a list in a reverse order.
print(l1[::-1])
'''

class check():
    def __init__(self):
        self.n=[]
    def add(self,a):
        return self.n.append(a)
    def remove(self,b):
        self.n.remove(b)
    def dis(self):
        return (self.n)
 
obj=check()
 
choice=1
while choice!=0:
    print("0. Exit")
    print("1. Add")
    print("2. Delete")
    print("3. Display")
    choice=int(input("Enter choice: "))
    if choice==1:
        n=int(input("Enter number to append: "))
        obj.add(n)
        print("List: ",obj.dis())
 
    elif choice==2:
        n=int(input("Enter number to remove: "))
        if n in obj.dis():
            obj.remove(n)
            print("List: ",obj.dis())
        else:
            print("Entered number not in object")
 
    elif choice==3:
        print("List: ",obj.dis())
    elif choice==0:
        print("Exiting!")
    else:
        print("Invalid choice!!")
 
print()
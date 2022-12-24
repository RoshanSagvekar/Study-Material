l1=[12,34,36,63,96,23,12]

#WAP to create the list of even number of l1 without using filter.

#Without comprehension
evenlist=[]
for value in l1:
    if value%2==0:
        evenlist.append(value)
print('List:',l1)
print('List of even number from l1 :',evenlist)

'''
    Comprehension:-
        Comprehension offers a shorter syntax to create any
         changeable(mutable) iterable object (list,set,dict)

    Instead of creating an empty list and then appending values
    to the list using for loop another simple way of doing so is as 

    if comprehension on list is known as List Comprehension.
    syntax:-
        iterable_variable=[expression from var_name in iterable]
        iterable_variable=[expression from var_name in iterable if condition]
'''
sqlist=[num**2 for num in l1]
print(sqlist)
#With Comprehension
evenlist=[num for num in l1 if num%2==0]
print('List Of Odd Numbers in l1:',evenlist)


#Create a set of even numbers from l1 using comprehension.
#Set Comprehension
evenset={num for num in l1 if num%2==0}
print('Set Of Odd Numbers in l1:',evenset)

#Dictionary Comprehension
'''
    Method of Shortest way to create dictionary.

    Syntax:-
            var_name={key_expr:value_expr for var in iterable if condition}
'''
l1=[2,43,54,65]
#WAP to create a dictionary using above list using comprehension
#list element as key and its square.

dict1={num:num**2 for num in l1}
print(dict1)
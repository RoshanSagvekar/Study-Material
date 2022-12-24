#  Program to check if element exists in list

"""list1=[1,2,3,4,5]

ele = int(input('Enter any element to check exist in list:'))
if ele in list1:
    print(ele,'exists in a list')
else:
    print(ele,'not exists in a list.')"""


# Different ways to clear a list in Python

"""list1 = [1,3,4,2,5,6]
print(list1)
list1.clear()
print(list1)"""

#  Reversing a List
"""
list1 = [1,2,4,5,6,7]
print("Before Reversing:",list1)
list1.reverse()
print("After Reversing using method:",list1)
list1 = list1[::-1]
print("Reversing list using slicing:",list1)
lis=[1,2,3]
l2 = []
for i in reversed(lis):
    l2.append(i)
print(l2)
"""

tuples = [(), ('ram','15','8'), (), ('laxman', 'sita'), ('krishna', 'akbar', '45'), ('',''),()]

def Remove(tuples):
    list1 = [t for t in tuples if t]
    return list1

print(Remove(tuples))
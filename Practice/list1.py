#Write a Python program to find the item with maximum occurrences in a given list.
'''
list1=[3,1,2,4,5,1,4,3,2,1,6,3,7,2,3,1,3]
val=0
result=0
for i in list1:
    a=list1.count(i)
    if a>val:
        val=a
        result=i
    result
print('Item with maximum appearance:-',result,'\nCount of',result,'=',list1.count(result))
'''
'''
my_string='Roshan'
k=[print(i) for i in my_string if i not in 'aeiou']

m=[[x,y] for x in range (0,4) for y in range(0,4)]
print(m)

t=(1,2,4,3)
p=t[1:3]
print(p)

d={'john':40,'peter':45}
var=d["john"]
print(var)

x=15
y=12
a=x&y
print(a)

x='abcd'
for i in x:
    print (i)
    x.upper()

var="abcd"[2:]
print(var)

dict={"Joey":1,"Rachel":2}
dict.update({"Phoebe":2})
print(dict)

a=list('hello')
print(a)
'''
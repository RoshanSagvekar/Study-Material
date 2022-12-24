#List of python datatype.
#int
num=123
print('num:- ',num,'it type is ',type(num))

#float
num1=12.4
print('num1:- ',num1,'it type is ',type(num1))

#String
name='Raj'
print('name:- ',name,'it type is ',type(name))

#Bool
flag=True #false
print('flag:- ',flag,'it type is ',type(flag))

#List:-Single Variable store a multiple values.
l1=[1,2.3,'Raj',True,[1,3]]         #Collection of heterogenous value
print('l1:- ',l1,'it type is ',type(l1))
#It is changeable
l1[0]=l1        #Accessing by the index it start from zero.
print('l1:-',l1)


#Tuple:-Single variable store multiple values.
t1=(1,3,4)      #it also collection of heterogenous value.
#or
t2=1,43,7   #here tuple can be modify.
#it can access by index but cannot be change.
print('t1:- ',t1,'it type is ',type(t1))
print('t2:- ',t2,'it type is ',type(t2))

#Set :-Single variable store a multiple values.
s1={11,2,43,'Raj',True} #it also collection of heterogenous value.
print('s1:- ',s1,'it type is ',type(s1))
#It is unorder.
#it cannot be access by index but it can change.


#Dictionary:-Collection of key-value pair
#Where key is unique and value may be datatype
d1={1:'a',2:'b',3:'c'}
print('d1:-',d1,'it datatype is ',type(d1))

#compex number:-Number which contain real number and imaginary number.
#real+imaginary
cn=3+2j
print('cn:-',cn,'its datatype is ',type(cn))






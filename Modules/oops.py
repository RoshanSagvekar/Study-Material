'''
    OOP Stands for object Oriented Programming Languages.
    OOP is concept followed by multiple programming langauge
    like C++,Python,Java,PHP,Javascript,C#,etc
'''
#What is Object Oriented Programming.
'''
    Object oriented programming is all about the "Objects".

    Object is a group of interrelated variable and function
    where 
    Variables are referred to as properties/Attributes of object.
    Function/Methods Are referred to the behaviour of the object.

    Object Provides the better and clear structure for the program.
    e.g
        A car can be an object.
        If it is object then 
        its properties are its color,its speed,its model etc.
        its behavior run(),acceleration(),break() etc.

    Before OOP there is Procedure Oriented Programming(POP)
    which used to define a program like C.

    Procedure is also known as function
    It based on function instead of object.
    and python has this feature also.
'''
#Major Python OOPs Concept/Principle:-
# 1.Class:-
'''
    ->Classes are template/blueprint of object.
    ->Class is collection objects.
    ->It is known as logical entity.
    ->Syntax:-
        class Class_name:
            class body
    ->E.g
        class car:  #Empty Class
            pass    #pass is keyword to define any block of code
'''

class car:
    pass
# 2.Objects:-
'''
    ->It is a instance of class.
    ->It has a state(properties) and behaviour(functionality).
    ->Syntax:-
        object_name=ClassName()
'''
"""
obj=car()
print(obj,type(obj))
print(isinstance(obj,car))
print(isinstance(obj,int))
"""





#Properties and behaviour of object.
"""
class car:
    #instance method
    def setProp(self):
        #instance variable
        self.color='Red'
        self.speed=40
    def run(self):
        print('Car is Running.')
        print("Self:-",self)
        print(f"My {self.color} car is running with {self.speed}km/hr speed.")
    
obj=car()
#behaviour
obj.setProp()
obj.run()
#Properties
obj.color='blue'
obj.speed=54
obj.run()
#another type of calling function of class.
car.run(obj)


#WAP to create a object of class student class with 2 properties.
#and using show method display property.

class student:
    def setproperty(self):
        self.id=101
        self.name='Raj'
    def show(self):
         print(f'Hello {self.name} your id is {self.id}')

std=student()
std.setproperty()
std.show()

# Circle():-
class circle:
    def setproperty(self,r):
       self.radius=r
    def cal_area(self):
        return(3.14*(self.radius**2))

c1=circle()
c1.setproperty(2.5)
print("Area of c1 circle is ",c1.cal_area())
c2=circle()
c2.setproperty(3.6)
print("Area of c2 circle is ",c2.cal_area())
"""
#Constructor
'''
    ->It is special method of the class which used to initialize
    the object with properties.

    ->In Python name of constructor of each class is same i.e
    def __init__(self):
        body constructor

    ->This constructor invoke/call automatically when the objcet of 
    class get created.

    ->In constructor we can define parameters also if needed.
      So there are 2 types of constructor.
      1.Non-Parameterized
        ->it set the default(same) value to each object.

      2.Parameterized
        ->It set the different value to each object.
'''
"""
class car:
    def __init__(self):
        self.color="red"
        self.speed=60.50
        print('Object is initialize with some properties.')   

    def run(self):
        print(f"My {self.color} car is running with {self.speed}km/hr speed.") 

#here we create the object of class after creating the object 
# python interpreter will invoke/call constructor of class if it define.
obj=car()
obj.run()
obj.color='Blue'
obj.speed=50
obj.run()

#Parameterized Constructor
class student:
    def __init__(self,i,n):
        self.id=i
        self.name=n

    def show(self):
        print(f'Hello {self.name} your id is {self.id}')

std=student(101,'Roshan')
std.show()
""" 
# Destructor
'''
    ->Desturctor is also special method of class which is used to destroy the object.
    ->And even it help to perform cleaning task on the object.

    Synatx:-
        def __del__(self):
            body destructor.
        
    ->It is also invoke automatically when the object delete 
     from the memory.

    ->In python destructor are not need as much in c++ because
      python has GC(garbage collector)

    -> Garbage Collector is used to delete the unused object
      from memory to release the memory used by them.
'''
"""
class demo:
    def show(self):
        print('Hii!')

    def __del__(self):
        print('Destructor is Invoke.')
        print('Object is deleted from memory.')

obj=demo()
obj.show()
#del obj
print('Program is Completed')
"""
#WAP a program to create a rectangle class with appropriate properties and behavior.
"""
class rectangle:
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def area(self):
        area=self.l*self.b
        print("Area of Rectangle:-",area,'sq.cm')
    def perimeter(self):
        per=2*self.l+2*self.b
        print("Perimeter of Rectangle:-",per,'cm')

rec=rectangle(12,10)
rec.area()
rec.perimeter()
"""
#__str__:-
'''
    __str__(self) is also one of the method of object class
    which used convert python object into string when we print
    object into print method.
'''
"""
class Student:
    def __init__(self,id=0,name='None'):
        self.id=id
        self.name=name
    def __str__(self):
        return f"Student[sid={self.id},sname={self.name}]"

s0=Student()
s1=Student(101,'Raj')
s2=Student(102,'Ram')
print(s0)
print(s1)
print(s2)


stdlist=[Student(),Student(101,'Raj'),Student(102,'Ram')]
print(stdlist[1])
print(stdlist)
"""

#__repr__(self)
'''
    It is also one of the method of object class which represent python into
    iterable type(list,tuple etc) in string format.
    otherwise it is similar to __str__.
'''
"""
class Student:
    def __init__(self,id=0,name='None'):
        self.id=id
        self.name=name
    def __repr__(self):
        return f"Student[sid={self.id},sname={self.name}]"

stdlist=[Student(),Stud ent(101,'Raj'),Student(102,'Ram')]
print(stdlist[1])
print('Student List:-',stdlist)
"""

#Static Members
'''
    In python we can create a static variable and static Methods.
'''
#Static Variale
'''
    When we declare a variable inside a class,but outside the method is called as static variable.

    Static Variable create a singlecopy and shared with all objectof same class.

    Static variable are access by the Class name.
    So it is also known as class variable.
'''
"""
class Student:
    sinstitute='ITvedant'   #static variable
    def __init__(self,id=0,name='None'):
        #Instance variable
        self.id=id
        self.name=name
    def __repr__(self):
        return f"Student[sid={self.id},sname={self.name}]"

s1=Student(id=101,name='Raj')
s2=Student(id=102,name='Rohan')
print("s1:-",s1.id,s1.name,s1.sinstitute)
print("s2:-",s2.id,s2.name,s1.sinstitute)
#print("Student Name:-",Student.name)
#instance variable can not access by class name.

print("Student Institute:-",Student.sinstitute)
Student.sinstitute='ABCs'
#Don't use object to change value of static variable.
print("s1:-",s1.id,s1.name,s1.sinstitute)
print("s2:-",s2.id,s2.name,s1.sinstitute)
"""

#Static Methods
'''
    Python has static methods that are belong to the class.
    It is similar to static variable that bounds to class rather
    than object of class.

    So we need to create any object of class to call the static method.
    it means we can directly call the static method with class name.

    Static methods are used to share the common behaviour with all instance 
    of class.

    Python interpreter will maintain single copy of static method 
    and shared with all object.

    Static method are declared by @Staticmethod decorator.
'''
"""
class Student:
    sinstitute='ITVedant'
    @staticmethod
    def welcome():
        print('Hello Students')
        print('Welcome to',Student.sinstitute)

#Static method without object i.e  with classname
Student.welcome()
s1=Student()
s1.welcome()
"""

#Principle of Object Oriented Programming
'''
    In OOPs,There are 4 Principle 
    1. Encapsulation
    2. Inheritance
    3. Polymorphism
    4. Data Abstraction
'''
# 1. Encapsulation
''' 
    Encapsulaton is one of the oops principle ,which is use to wrap a
    data into single unit.

    It is used to protect data of object from outside world.

    It is achieve in python using private variable.
    Private variables are those variable prefix with __
    and we can access them into class only.

    To access the private variable outside a class 
    we use getter method and setter method which known 
    as Accessors in python
''' 

#Class With Private Variable.
"""
class Student:
    def __init__(self,sid,sname):
        #Private variable (access in class only i.e with self keyword only.)
        self.__sid=sid
        self.__sname=sname

    #getters
    def getsid(self):
        return self.__sid
    def getname(self):
        return self.__sname
    
    #setters
    def setsid(self,sid):
        self.__sid=sid

s1=Student(101,'Raj')
print('Id:-',s1.getsid())
print('Name:-',s1.getname())
s1.setsid(102)
print("Id:-",s1.getsid())
"""

# 2.Inheritance
'''
    Inheritance is also one  of the oops principle.
    in which newly created class can access properties of another class

    The main advantage of inheritance is used to achieve Reusablity of code.

    Syntax:-
	    class Existing_Class:
		    .....
	
	    class New_class(Existing_class)
		    ....

	here,
        Existing_class is known as Parent class or also known as 
        Super class or Base Class.

        New class is known as Child class or Sub class or 
        Derived class.

'''
"""
class Person:
    def setdata(self):
        self.fname='Raj'
        self.lname='Sharma'

class Student(Person):
    def showdata(self):
        print("First Name:-",self.fname)
        print("Last Name:-",self.lname)
    
std=Student()
std.setdata()
std.showdata()
print(isinstance(std,Student))
print(isinstance(std,Person))
print(isinstance(std,object))
'''
-Here object is built-in python class
-It is default 1st parent of all the classes of python.
-The object provides basic features to each of python.
    like object creation,constructor,destructor,__str__, __repr__.
'''
"""
# Inheritance with Constructor
"""
class Person(object):
    def __init__(self):
        print("Constructor of Person Class.")

class Student(Person):
    def __init__(self):
        super().__init__()
        # here super() is method.
        # It is used to invoke parent class method from child class.
        print("Constructor of Student Class.")

std=Student()
"""

# Inheritance with Parameterized Constructor
"""
class Person(object):
    def __init__(self,fname):
        self.fname=fname
        print("Constructor of Person Class.")
        print('First Name:-',fname)

class Student(Person):
    def __init__(self,fname):
        super().__init__(fname)
        print("Constructor of Student Class.")

std=Student('Raj')
print("Student name is",std.fname)
"""

# Types of Inheritance
'''
    In Python,
        There are 5 Types of inheritance
        1.Single Inheritance
            The inheritance program which one single parent and child 
            class is known as Single.

            e.g The above examples.

        2.Multilevel Inheritance.
            In inheritance program if child class having one more child class is 
            known as Multilevel inheritance.

            It represents   Grand_Parent-Parent-Child relationship

'''
#Example of Multilevel inheritance.
"""
class Person:
    def personinfo(self):
        print('This is a Person class with Personal details')
    
class Employee(Person):
    def salaryinfo(self):
        print('This is a Employee class with Salary details')
    
class Manager(Employee):
    def bonusinfo(self):
        print("This is Manager class with Bonus details.")

# 1st Child
print('Employee')
emp=Employee()
emp.personinfo()
emp.salaryinfo()

#Child of child
print('Manager')
mgr=Manager()
mgr.bonusinfo()
mgr.salaryinfo()
mgr.personinfo()
"""

# 3.Hierarchichal Inheritance:-
'''
    In this type one single parent class having 2 or more 
    child classes is known hierarchichal.

    Person <---- Customer
    Person <---- Employee
    Customer is a Person but not Employee.
    Employee is a Person but not Customer. 
'''
"""
class Person:
    def personinfo(self):
        print("This is a Person Class with personal details")
        
class Employee(Person):
    def salaryinfo(self):
        print("This is a Employee Class with Salary details")
                
class Customer(Person):
    def shoppinglist(self):
        print("This is a Customer Class with shopping list")
        
print("Employee")
emp = Employee()
emp.personinfo()
emp.salaryinfo()

print("Customer")
cust = Customer()
cust.personinfo()
cust.shoppinglist()
"""

# 4. Multiple Inheritance
'''
    In this one single child class with 2 or more Parent Class.
'''
"""
class Human:
    def walk(self):
        print('Human can walk')

class Animal:
    def jump(self):
        print('Animal can Jump')

class Vampire(Human,Animal,):
    pass

vam=Vampire()
vam.walk()
vam.jump()
"""

# 5.Hybrid Inheritance
'''
    It is combination of all the types of inheritance.
'''
#Example is Home Work Task......

# Polymorphism
'''
    Polymorphism:-
    poly --> many.
    morphism --> form,shapes.

    The literal meaning of polymorphism is the many form.

    Polymorphism is a very important oop principle.
    It referes to the use of single property or method differently in 
    different scenarios.
'''
"""
# Addition of integer
n1=12
n2=13
print(n1+n2)
n1='12'
n2='13'
print(n1+n2)

#Built in Function with polymorphism
print(len('Raj'))
print(len(['Raj','Jay']))
print(len({1:'Raj',2:'Jay',3:'Rosh'} ))
"""
'''
len is single function which diffrently work for each object
str  --> Count the number of characters
list --> Count the number of Value
dict --> Count the number of Pair
'''

#Polymorphism with user classes
'''
    WE can achieve polymorphism in python using 
    Method Overriding:-
        Parent and child class have Method with same name is known as 
        Method Overriding
'''
"""
class Animal:
    def eat(self):
        print('Every Animal eat Something.')

obj1=Animal()
obj1.eat()

class Dog(Animal):
    def eat(self):
        super().eat()   # To call Parent Class Method.
        print('Every dog loves to eat bones.')

obj2=Dog()
obj2.eat()
"""

# Overriding with Multiple inheritance.
"""
class A:
    def m1(self):
        print('Method of Class A')

class B:
    def m1(self):
        print('Method of Class B')

class C(A,B):
    def m1(self):
        super().m1()    #it will 1st Parent.
        B.m1(self)
        print('Method of Class C')

obj=C()
obj.m1()
"""

# Operator Overloading
'''
    + operator 
    Using with integer variable then it will add them.
    using with string variable it will concat.

    It is known as Operator Overloading.
    Single python operator performing 2 or more task
    The task of this operator are fixed i.e
    + operator is use with number only and str

    -can we overload this operator with user define object?
    -Yes.
'''
# Operator Overloading with user define object.
"""
class Circle:
    def __init__(self,radius):
        self.radius=radius
    #Operator overloading
    def __lt__(self,other):
        return self.radius< other.radius
    
    def __add__(self,other):
        return Circle(self.radius+other.radius)

c1=Circle(2.5)
c2=Circle(3.5)
print(c1<c2)
print(c1>c2)
c3=c1+c2
print(c3,type(c3))
print(c1,c1.radius)
print(c2,c2.radius)
print(c3,c3.radius)
"""

# 4.Data Abstraction
'''
    Abstraction is also one of the important oops principle.

    It is used to hide internal functionality of function from outside world(user).

    User is familiar with the what that function does but they don't 
    know how it does.

    It is used to avoid the complexity of application by hiding 
    irrelevant details.
'''
#How to achieve Abstraction in Python?
'''
    The Abstarction can be achieve by the abstract classes and methods.
'''
# What is Absract class?
'''
    A class that consist of one or more abstract method is called as
    Abstract Class.

    In python ,Abstract class must be inherit to Abc class of abc module.

    Syntax:
        From abc import ABC
        class Class_Name(Abc):
            body of class
'''

# What is Absract Method?
'''
    An Abstract method is method which is declared without any body
    (implementation)
    i.e Empty method is known as Abstract method.

    And also declared with @abstractmethod decorator of abc method
'''
#Example
from abc import ABC, abstractmethod
class Shape(ABC):

    @abstractmethod
    def draw(self):
        pass # Without implementation
    @abstractmethod
    def area(self):
        pass

#obj=Shape()
# Abstract class can't be instantiate(i.e Can't Create the object of Abstract class.)

class Circle(Shape):
    def draw(self):
        print("Draw The Circle")
    def Circumference(self):
        return'Circumference of circle'
    def area(self):
        return 'Area of Circle.'

# If you inherit an abstract class,it must be implement all the abstract
# method of that class otherwise child class also become abstract class.

cir=Circle()
print(cir.Circumference())
cir.draw()
print(cir.area())

"""
class School:
    def func1(self):
        print('This function is in school')

class Student1(School):
    def func2(self):
            print('This function is in Studen1')

class Student2(School):
    def func3(self):
        print('This function is in Student2')

class Student3(Student1,School):
    def func4(self):
        print('This function is in Student3')

obj=Student3()
obj.func1()
obj.func2()
"""
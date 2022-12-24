# Write a program to perform CRUD operations using OOP concepts,we store details of student.
'''
    Student:
        Name
        Mobile
        Email
 For CRUD utilize list,List of student object

 The program should an infinite loop,a loop that continue till user wishes.
'''

# Global variable for student list.
student_list=[]

# Class creation of the student 
class student:
    def __init__(self,name,email,mobile):
        self.name=name;self.email=email;self.mobile=mobile
    
    def update_details(self,name,email,mobile):
        self.name=name;self.email=email;self.mobile=mobile
    
    def __str__(self):#overloading the existing __str__ ()
        return "{}-{}-{}",format(self.name,self.email,self.mobile)

# file details
#file=open("Student.txt","a+")

# Skeleton for infinite loop

while True:
    print("""1.To insert Student\n2.To Update Student Details\n3.To Delete Student\n4.To View all Student\n5.Quit Program""")
    try:
        ch=int(input('Enter your choice='))
        if ch==1:
            name,email,mobile=input('\tEnter a name='),input('\tEnter e-mail='),input('\tEnter mobile=')
            student_list.append(student(name,email,mobile))
            #file.write(str(student_list[-1]))
            #file.write("\n")

        elif ch==2:
            for i in range(len(student_list)):
                print(f"{i+1}{student_list[i]}")
            c=int(input('Enter number which you want to update='))
            name,email,mobile=input('\tEnter a name='),input('\tEnter e-mail='),input('\tEnter mobile=')
            student_list[c-1].update_details(name,email,mobile)

        elif ch==3:
            for i in range(len(student_list)):
                print(f"{i+1}{student_list[i]}")
            c=int(input('Enter number which you want to delete='))
            student_list.pop(c-1)

        elif ch==4:
            for student in student_list:
                # call for in-built string converted function __str__()
                print(student)

        elif ch==5:
            break
        else:
            print('Wrong input')
    except:
        print('Wrong input')

#file.close()




# Serialization and Deserialization




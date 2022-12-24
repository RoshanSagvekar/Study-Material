#import library for serialization and deserialization
import pickle as p
#global variable for student list:
student_list = []

#Class creation of the student
class Student:
    def __init__(self, name, email, mobile):
        self.name=name; self.email = email; self.mobile=mobile

    def update_details(self, name, email, mobile):
        self.name=name; self.email = email; self.mobile=mobile

    def __str__(self): #overloading the existing __str__() function
        return "{} - {} - {}".format(self.name, self.email, self.mobile)
        
#file details
#file = open("students.txt", "a+")
try:
    file=open("students.dat","rb+")
    for line in file.readlines():
        student_list.append(p.loads(line))
    file.close()
except Exception as e:
    print(e)

# Skeleton for infinte loop
while True:
    print("""1. Add Student
2. Update Student Details
3. Delete Student
4. View all Students
5. Quit Program""")
    try:
        ch = int(input("Enter your choice:"))
        if ch==1:
            name, email, mobile = input("Enter a name:"), input("Enter E-mail id:"), input("Enter mobile number:")
            student_list.append(Student(name, email, mobile))
            #file.write(str(student_list[-1]))
            #file.write("\n")
        elif ch==2:
            for i in range(len(student_list)):
                print(f"{i+1} {student_list[i]}")
            c = int(input("Enter the number you wish to update:"))
            name, email, mobile = input("Enter a name:"), input("Enter email id"), input("Enter mobile number")
            student_list[c-1].update_details(name, email, mobile)
        elif ch==3:
            for i in range(len(student_list)):
                print(f"{i+1} {student_list[i]}")
            c = int(input("Enter the number you wish to delete:"))
            student_list.pop(c-1)
        elif ch==4:
            for student in student_list:
                #calls for in-built string converted function __str__()
                print(student)
        elif ch==5:
            file=open('students.dat',"wb")
            for student in student_list:
                file.write(p.dumps(student))
                file.write(bytes("\n","ascii"))
            file.close()
            break
        else:
            print("Invalid Choice")
    except Exception as e:
        print("Wrong input")
        print(e)
    

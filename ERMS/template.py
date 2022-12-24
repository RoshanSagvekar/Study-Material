from model import Employee
import view as v
import os 

choice=0
while choice!=6:
    print('-*-'*3,'EMPLOYEE RECORD MANAGEMENT SYSTEM','-*-'*3)
    print('\n\t1.Add Employee')
    print('\t2.Show All Employee')
    print('\t3.Show Employee by ID')
    print('\t4.Update Employee')
    print('\t5.Delete Employee')
    print('\t6.Exit')
    choice=int(input('\nEnter Your Choice='))
    os.system('cls')

    if choice==1:
        emp=Employee() # object with default value

        # Here replace the value with user inputs.
        emp.empid=int(input('\tEnter Employee ID='))
        emp.empname=input('\tEnter Employee Name=')
        emp.empsalary=float(input('\tEnter Employee Salary='))

        v.save(emp)

    elif choice==2:
        elist = v.getAll()
        print('-+-'*10,"Employee List",'-+-'*10)
        print()
        for emp in elist:
            print('\t\t',emp)

    elif choice==3:
        empid=int(input('\tEnter Employee ID to Search='))
        emp=v.getEmployee(empid)
        if empid!=None:
            print('\tEmployee Found')
            print('\t',emp)
    
    elif choice==4:
        empid=int(input('\tEnter Employee ID to Update='))
        emp=v.getEmployee(empid)
        if emp!=None:
            print('\tEnter Updated Details=')
            print('\t',emp)
            newemp=Employee()
            newemp.empname=input('\tEnter Employee Name=')
            newemp.empsalary=float(input('\tEnter Employee Salary='))

            v.update(empid,newemp)
            print('\tEmployee is Updated.')
        else:
            print('\tInvalid Employee Id........!')

    elif choice==5:
        empid=int(input('\tEnter Employee ID to Delete='))
        emp=v.getEmployee(empid)
        if emp!=None:
            v.delete(empid)
            print('\tEmployee Deleted Successfull.')
        else:
             print('\tInvalid Employee Id........!')

    elif choice==6:
        print('\t\tThank You....!')
    else:
        print('\tInvalid Choice')
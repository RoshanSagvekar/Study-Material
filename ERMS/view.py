from model import Employee

#Global Object
emplist=[]
# Object with Reference
emp=Employee(101,'Raj',25000)
emplist.append(emp)

# Without Reference
emplist.append(Employee(102,'Jay',35000))

# Create
def save(emp):
    emplist.append(emp)
    print('Employee is Added Successfully.')

# Read All object
def getAll():
    return emplist

# Read Single object
def getEmployee(empId):
    l1=list(filter(lambda emp:emp.empid==empId,emplist))
    if len(l1)==1:
        return l1[0]
    else:
        print('\tEmployee Not Found')

# Update 
def update(empid,newemp):
    emp=getEmployee(empid)  #find which we want to update
    index=emplist.index(emp)    # index its index    
    emplist[index].empname=newemp.empname   # replace with new value
    emplist[index].empsalary=newemp.empsalary

# Delete
def delete(empid):
    emp=getEmployee(empid)  #find which we want to delete
    index=emplist.index(emp)
    emplist.pop(index)



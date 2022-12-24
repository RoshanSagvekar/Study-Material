#Create a function showEmployee() in such a way that it should accept employee name,
# and its salary and display both.
# If the salary is missing in the function call assign default value 9000 to salary.

def showEmployee(name,sal=9000):
    print('\t\t"Employee Info"')
    print('\tEmployee Name:-',name)
    print('\tSalary:-',sal)

showEmployee('Roshan',12000)
showEmployee('Suraj')


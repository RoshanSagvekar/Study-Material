#It is my employee model which represent employee details.
class Employee:
    def __init__(self,empid=0,empname='',empsalary='0.0'):
        self.empid=empid
        self.empname=empname
        self.empsalary=empsalary
    
    def __repr__(self):
        return f'Employee[{self.empid},{self.empname},{self.empsalary}]'
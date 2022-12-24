#A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years.
   #Ask user for their salary and year of service and print the net bonus amount.
"""
sal=int(input('Please Enter Your Salary='))
year=int(input('Please Enter your year of service='))
if(year>5):
    bonus=sal*0.05
    print('Congrats!You have ',bonus,'rupees bonus.')
else:
    print('Sorry!You do not have bonus.')

"""
"""
n1=int(input('Enter a number='))
n2=int(input('Enter a number='))
quo=n1/n2
rem=n1%n2
print('Quotient=',quo)
print('Remainder=',rem)
"""

"""

l1=[1,2,3,4,5,6,7]
l2=[1,5,9,7,6,4,2]
def union(l1,l2):
    l3=[]
    for i in l1:
            if i in l2:
                l3.append(i)
    print(l3)
union(l1,l2)

"""



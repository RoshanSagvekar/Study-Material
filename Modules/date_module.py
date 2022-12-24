'''
WAP to demonstrate all the methods in datetime module

-> datetime
     - year
     - month
     - day
     - timedelta
     - strftime
     - datetime.strptime

-> time
    - hour
    - minute
    - second
'''
"""
import datetime
from time import strftime, time

x=datetime.datetime.now()
print('Current date & time:-',x)
print('Year:-',x.year)
print('Month:-',x.month)
print('Day:-',x.day)

y=datetime.date(year=2021,month=5,day=26)
print('Month in word:-',y.strftime("%B"))
print('Day in word:-',y.strftime("%A"))

today=datetime.datetime.today()
day=today+datetime.timedelta(days=1,weeks=1)
print('Date after 1 week and 1 day from today=',day)

date=input('Enter Date in format (DD-MM-YYYY)=')
pdate=datetime.datetime.strptime(date,'%d-%m-%Y')
print(pdate)

t=datetime.time(12,25,35)
print('Hour:-',t.hour)
print('Minute:-',t.minute)
print('Second:-',t.second)
"""

#strptime used to covert string date into
# datetime type with specific  format
'''
import datetime as dt
today = dt.date.today()
print(today,type(today))
today = dt.datetime.today()
print(today,type(today))

today = '14-Jun-2021'
print('Today:- ',today,type(today))

today2 = dt.datetime.strptime(today,'%d-%b-%Y')
print('Today:- ',today2,type(today2))
'''
# 1.Write a Python program to print yesterday, today, tomorrow.
"""
import datetime as dt
today=dt.date.today()
yesterday=today-dt.timedelta(1)
tomorrow=today+dt.timedelta(1)
print('Today:-',today)
print('Yesterday:-',yesterday)
print('Tomorrow:-',tomorrow)
"""
# 2.Write a Python program to print next n days starting from today.

"""
import datetime as dt
from time import strftime
x=dt.date.today()
n=int(input('Enter number of days from today='))
for i in range(0,n):
    day=x+dt.timedelta(i)
    print(day,day.strftime('%A'))
"""

#1.write a program to accept date of birth of actor and calculate age of actor use datetime module.

import datetime as dt
bdate=input('Enter your date of birth in format(YYYY-MM-DD)=')
year,month,day=map(int,bdate.split('-'))
date=dt.date(year,month,day)
age=(dt.date.today()-date).days//365
print('Your Age=',age,'years')


# 2.Create Module CalculationAoprations  with function add mul,sub div and
# access this function from a file named Test

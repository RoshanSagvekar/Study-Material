from typing import Coroutine
import pymysql
from werkzeug import datastructures
con=pymysql.connect(user="root",passwd="",host="localhost",database="python_demo")
cur=con.cursor()
selectq="SELECT * FROM student;"
cur.execute(selectq)

# implemettion of fetchall
"""
t=cur.fetchall()
for rollno,name,email,mobile in t:
    print(rollno,name,email,mobile)
"""
# implementation of fetchone
"""
t=cur.fetchone()
print(t)
"""

# implemetation of fetchmany

t=cur.fetchone()[2]
print(t)
"""

import pymysql
con=pymysql.connect(user="root",passwd="",host="localhost",database="python_demo")
cur=con.cursor()
selectq="SELECT * FROM student WHERE rollno=%s;"
rollno=input('Enter rollno:')
cur.execute(selectq,rollno)
data=cur.fetchone()
print(data,type(data))
"""


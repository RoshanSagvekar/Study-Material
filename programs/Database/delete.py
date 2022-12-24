import pymysql
con=pymysql.connect(user="root",passwd="",host="localhost",database="python_demo")
cur=con.cursor()
deleteq="DELETE FROM student WHERE rollno=%s;"
rollno=input('Enter Roll no to delete record:')
cur.execute(deleteq,rollno)
con.commit()
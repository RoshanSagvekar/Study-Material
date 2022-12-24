import pymysql
con=pymysql.connect(user="root",passwd="",host="localhost",database="python_demo")
cur=con.cursor()
# updateq="""UPDATE student SET email="ashish@gmail.com" WHERE rollno=8;"""
updateq="UPDATE student SET email=%s WHERE rollno=%s;"
rollno,email=input('Enter Roll no:'),input('Enter email:')
cur.execute(updateq,(email,rollno))
con.commit()
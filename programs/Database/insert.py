import pymysql
# created connectin object
con=pymysql.connect(user="root",passwd="",host="localhost",database="python_demo")
#print(con)
cur=con.cursor()
#print(cur)

#insert_query="""INSERT INTO student (name,email,mobile)VALUES('Shravani Raut','shravani@yahoo.com',7854961534);"""
#cur.execute(insert_query)
#con.commit()

insertq="INSERT INTO student(name,email,mobile)VALUES(%s,%s,%s);"
name,email,mobile=input("Name:"),input("Email:"),input("Mobile:")
cur.execute(insertq,(name,email,mobile))
con.commit()

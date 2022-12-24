from flask import Flask
# render_template is a function that accepts the HTML page name.
from flask import render_template ,request,redirect ,url_for
import pymysql

# Creating a Flask object
app=Flask(__name__)

def load_pending_task_from_DB():
    con=pymysql.connect(user="root",password="",host="localhost",database="python_demo")
    cur=con.cursor()
    cur.execute("SELECT * FROM todolist WHERE status=0;")
    data=cur.fetchall()
    cur=cur.close()
    con.close()
    return data

def load_completed_task_from_DB():
    con=pymysql.connect(user="root",password="",host="localhost",database="python_demo")
    cur=con.cursor()
    cur.execute("SELECT * FROM todolist WHERE status=1;")
    data=cur.fetchall()
    cur=cur.close()
    con.close()
    return data

# To create a URL router,above the function
# use the annotation/decorator
# @app.route("url string",methods=[pass the list of
# supporting http methods])

@app.route('/',methods=['GET'])
def index():
    #return "Hello Flask Programming."
    return render_template("home.html")

@app.route('/pending_task',methods=['GET'])
def view_pending_tasks():
    # Connect to the database
    # Fetch all record where status=0
    data=load_pending_task_from_DB()
    # Render data to the html page.
    return render_template("pending.html",data=data)

def insert_task_to_DB(title,desc,date):
    con=pymysql.connect(user="root",password="",host="localhost",database="python_demo")
    cur=con.cursor()
    insertq="INSERT INTO todolist (task_title,task_description,doc)VALUES(%s, %s, %s);"
    cur.execute(insertq,(title,desc,date))
    con.commit()
    cur.close()
    con.close()

@app.route("/add_task", methods=['GET', 'POST'])
def add_new_task():
    # Check for POST Method
    if request.method == 'POST':
        # Load form data
        data = request.form #dictionary {'txtTitle':value, }
        # Storing the received Data into Database
        insert_task_to_DB(data['txtTitle'], data['txtDesc'], data['txtDate'])
        # Redirect to Pending Task 
        # url_for is used to create full URL
        # Redirect is used to call the created url
        return redirect(url_for("view_pending_tasks"))
    # Loading Empty Form
    return render_template("insert.html")

@app.route('/completed_task/',methods=['GET'])
def view_completed_task():
    # Connect to the database
    # Fetch all record where status=1
    data=load_completed_task_from_DB()
    # Render data to the html page.
    return render_template("completed.html",data=data)

def update_task_as_completed_to_DB(task_id):
    con=pymysql.connect(user="root",password="",host="localhost",database="python_demo")
    cur=con.cursor()
    cur.execute("UPDATE todolist SET status=1 WHERE id=%s;",(task_id))
    con.commit()
    cur.close()
    con.close()
    
# mark as completed
# http://127.0.0.1:5000/completed?id=1
@app.route("/completed")
def completed_task():
    # From URL get id
    task_id=request.args.get('id',type=int,default=1)
    update_task_as_completed_to_DB(task_id)
    return redirect(url_for("view_pending_tasks"))

# Delete 
# http://127.0.0.1:5000/delete?id=1
def delete_task_from_DB(task_id):
    con=pymysql.connect(user="root",password="",host="localhost",database="python_demo")
    cur=con.cursor()
    cur.execute("DELETE FROM todolist WHERE id=%s;",(task_id))
    con.commit()
    cur.close()
    con.close()

@app.route("/delete")
def delete_task():
    # From URL get id
    task_id=request.args.get('id',type=int,default=1)
    delete_task_from_DB(task_id)
    return redirect(url_for("view_pending_tasks"))
# Call the Flask object to execute the project.
if __name__ =='__main__':
    app.run(debug=True)
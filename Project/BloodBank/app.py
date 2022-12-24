from os import error
import re
from flask import Flask
from flask import render_template ,request,redirect ,url_for,session
import pymysql

# Creating a Flask object
app=Flask(__name__)


@app.route('/',methods=['GET'])
def index():
    return render_template("home.html")

def insert_details_to_DB(name,mobile,email,pwd,bgrp,bdate,state,dist,city):
    con=pymysql.connect(user="root",password="admin",host="localhost",database="bloodbank")
    cur=con.cursor()
    insertq="INSERT INTO userdetails (name,mobile,email,password,blgrp,bdate,gender,state,city)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s);"
    cur.execute(insertq,(name,mobile,email,pwd,bgrp,bdate,state,dist,city))
    con.commit()
    cur.close()
    con.close()

@app.route('/register',methods=['GET','POST'])
def register():
    if request.method=='GET':
        return render_template("register.html")
    # Check for POST Method
    elif request.method == 'POST':
        # Load form data
        data = request.form #dictionary {'txtTitle':value, }
        # Storing the received Data into Database
        insert_details_to_DB(data['Name'], data['mobile'],data['email'],data['pwd'], data['blgrp'], data['bdate'], data['gender'],data['state'], data['city'])
        # Redirect to Pending Task 
        # url_for is used to create full URL
        # Redirect is used to call the created url
        return redirect(url_for("index"))

# Log in

def load_id_from_DB(email,pwd):
    con=pymysql.connect(user="root",password="admin",host="localhost",database="bloodbank")
    cur=con.cursor()
    selectq="SELECT id FROM userdetails WHERE email=%s AND password=%s;"
    cur.execute(selectq,(email,pwd))
    con.commit()
    cur.close()
    con.close()


@app.route('/login',methods=['GET','POST'])
def login():
    error = ""
    if 'username' in session:
        return redirect(url_for('index'))
    elif request.method == 'POST':
        username_form  = request.form['email']
        password_form  = request.form['pwd']
        con=pymysql.connect(user="root",password="admin",host="localhost",database="bloodbank")
        cur=con.cursor()
        cur.execute("SELECT COUNT(1) FROM userdetails WHERE email = %s;", [username_form]) # CHECKS IF USERNAME EXIST
        if cur.fetchone()[0]:
            cur.execute("SELECT password FROM userdetails WHERE email = %s;", [username_form]) # FETCH THE PASSWORD
            for row in cur.fetchall():
                if password_form == row[0]:
                    session['username'] = request.form['email']
                    return redirect(url_for("profile"))
                else:
                    error="Invalid Credential...!"
        else:
            error="Invalid Credential....!"
    return render_template('login.html', error=error)

        
# Log out

@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)
    return redirect(url_for('login'))


# Search Blood

def load_blood_from_DB(blgrp,city):
    con=pymysql.connect(user="root",password="admin",host="localhost",database="bloodbank")
    cur=con.cursor()
    selectq="SELECT id,name,mobile,email,blgrp,gender,city FROM userdetails WHERE blgrp=%s AND city=%s;"
    cur.execute(selectq,(blgrp,city))
    data=cur.fetchall()
    cur=cur.close()
    con.close()
    return data

@app.route('/findblood/',methods=['GET','POST'])
def find_blood():
    if request.method=='GET':
        return render_template("findblood.html")
    elif request.method=='POST':
        args=request.form
        data=load_blood_from_DB(args['blgrp'],args['city'])
        # Render data to the html page.
        return render_template("findblood.html",data=data)

# Request Blood

def insert_patientdetails_to_DB(pname,blgrp,state,city,hname,cname,mobile,need_date,reason):
    con=pymysql.connect(user="root",password="admin",host="localhost",database="bloodbank")
    cur=con.cursor()
    insertq="INSERT INTO patientdetails (pname,blgrp,state,city,hname,cname,mobile,need_date,reason)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s);"
    cur.execute(insertq,(pname,blgrp,state,city,hname,cname,mobile,need_date,reason))
    con.commit()
    cur.close()
    con.close()

@app.route('/requestblood',methods=['GET','POST'])
def requestblood():
    if request.method=='GET':
        return render_template('requestblood.html')
    elif request.method == 'POST':
        data = request.form
        insert_patientdetails_to_DB(data['pname'], data['blgrp'],data['state'],data['city'], data['hname'], data['cname'], data['mobile'], data['date'], data['msg'])
        return redirect(url_for("index"))


# dashboard

def load_user_data_from_DB(email):
    con=pymysql.connect(user="root",password="admin",host="localhost",database="bloodbank")
    cur=con.cursor()
    selectq="SELECT id,name,mobile,email,blgrp,city,gender,state FROM userdetails WHERE email=%s;"
    cur.execute(selectq,(email))
    data=cur.fetchall()
    cur=cur.close()
    con.close()
    return data

def update_data_from_DB(id):
    con=pymysql.connect(user="root",password="admin",host="localhost",database="bloodbank")
    cur=con.cursor()
    updateq="UPDATE FROM userdetails SET name=%s,gender=%s,mobile=%s,email=%s,blgrp=%s,city=%s,state=%s WHERE id=%s;"
    cur.execute(updateq,(id))
    con.commit()
    cur.close()
    con.close()

@app.route('/dashboard',methods=['GET','POST'])
def profile():
    if request.method=='GET':
        return render_template("dashboard.html")
    elif request.method=='POST':
        args=request.form
        data=load_user_data_from_DB(args['uname'])
        return render_template('dashboard.html',data=data)
    
# PROFILE

@app.route('/view_profile',methods=['GET','POST'])
def view_profile():
    if request.method=='GET':
        email=request.args.get('uname',type=str)
        data=load_user_data_from_DB(email)
        return render_template('view_profile.html',data=data)
    elif request.method=='POST':
        name=request.form['name']
        gender=request.form['gender']
        mno=request.form['mno']
        email=request.form['email']
        blgrp=request.form['blgrp']
        city=request.form['city']
        state=request.form['state']
        uid=request.form['uid']
        update_data_from_DB(name,gender,mno,email,blgrp,city,state,uid)
        return redirect(url_for('view_profile'))

def load_requests_from_DB():
    con=pymysql.connect(user="root",password="admin",host="localhost",database="bloodbank")
    cur=con.cursor()
    cur.execute("SELECT pid,pname,blgrp,cname,mobile,need_date,hname,reason,city,state FROM patientdetails WHERE status=0;")
    data=cur.fetchall()
    cur=cur.close()
    con.close()
    return data

# DONATE BLOOD
@app.route('/donateblood',methods=['GET'])
def donate():
    data=load_requests_from_DB()
    return render_template("donateblood.html",data=data)

app.secret_key = 'A0Zr98j/3yXR~XHH!jmN]LWX/,?RT'
# Call the Flask object to execute the project.
if __name__ =='__main__':
    app.run(debug=True)
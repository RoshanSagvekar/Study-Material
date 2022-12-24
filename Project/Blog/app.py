from datetime import date
from flask import Flask,render_template ,request,session,url_for,redirect,flash
import json,os,math
from werkzeug.utils import secure_filename
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


with open('config.json','r') as c:
    params=json.load(c)['params']

app=Flask(__name__)
app.secret_key = 'super-secret-key'
app.config['UPLOAD_FOLDER']=params['upload_location']
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:admin@localhost/blog'
db = SQLAlchemy(app)
# engine = create_engine('mysql+pymysql://root:@localhost/blog')



class Contacts(db.Model):
    srno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80),nullable=False)
    email = db.Column(db.String(120), nullable=False)
    phone_num = db.Column(db.String(120), nullable=False)
    msg = db.Column(db.String(120),nullable=False)
    date = db.Column(db.String(12), nullable=False)

class Posts(db.Model):
    srno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80),nullable=False)
    tagline = db.Column(db.String(80),nullable=False)
    slug = db.Column(db.String(120), nullable=False)
    content = db.Column(db.String(120), nullable=False)
    img_file=db.Column(db.String(12), nullable=False)
    date = db.Column(db.String(12), nullable=False)

@app.route('/')
def index():
    posts=Posts.query.filter_by().all()
    last=math.ceil(len(posts)/int(params['no_of_post']))
    page=request.args.get('page')
    if (not str(page).isnumeric()):
        page=1
    page=int(page)
    posts=posts[(page-1)*int(params['no_of_post']):(page-1)*int(params['no_of_post'])+int(params['no_of_post'])]
    # Pagination Logic
    # First
    if (page==1):
        prev="#"
        next="/?page="+str(page+1)
    elif (page==last):  # Last Page
        prev="/?page="+str(page-1)
        next="#"
    else:      # Middle page 
        prev="/?page="+str(page-1)
        next="/?page="+str(page+1)

    return render_template("index.html",params=params,posts=posts,prev=prev,next=next)

@app.route('/contact',methods=['GET','POST'])
def contact():
    if request.method=='POST':
        '''Add entry to database'''
        name=request.form.get('name')
        email=request.form.get('email')
        phone=request.form.get('phone')
        message=request.form.get('message')
        data=Contacts(name=name,email=email,phone_num=phone,msg=message,date=datetime.now())
        db.session.add(data)
        db.session.commit()
        flash('Thanks for submiting your details.We will get back to you soon.',"success")
    return render_template("contact.html",params=params)

@app.route('/about')
def about():
    return render_template("about.html",params=params)

@app.route('/post/<string:post_slug>',methods=['GET'])
def post_route(post_slug):
    post=Posts.query.filter_by(slug=post_slug).first()
    return render_template("post.html",params=params,post=post)

@app.route('/dashboard',methods=['GET','POST'])
def login_form():
    if ('user' in session and session['user']==params['admin_user']):
        posts=Posts.query.all()
        return render_template('dashboard.html',params=params,posts=posts)

    if request.method=='POST':
        username=request.form.get('uname')
        password=request.form.get('pwd')
        if (username==params['admin_user'] and password==params['admin_password']):
            # set the session variable
            session['user']=username
            posts=Posts.query.all()
            return render_template('dashboard.html',params=params,posts=posts)

    return render_template('login.html',params=params)


@app.route('/edit/<string:srno>',methods=['GET','POST'])
def edit(srno):
    if ('user' in session and session['user']==params['admin_user']):
        if request.method=='POST':
            title=request.form.get('title')
            tline=request.form.get('tline')
            slug=request.form.get('slug')
            content=request.form.get('content')
            img_file=request.form.get('img_file')
            date=datetime.now()

            if srno=='0':
                post=Posts(title=title,tagline=tline,slug=slug,content=content,img_file=img_file,date=date)
                db.session.add(post)
                db.session.commit()
                flash('Post Added Successfully.',"success")
            else:
                post=Posts.query.filter_by(srno=srno).first()
                post.title=title
                post.tagline=tline
                post.slug=slug
                post.content=content
                post.img_file=img_file
                post.date=date
                db.session.commit()
                flash('Post Updated Successfully.',"success")
                return redirect('/edit/'+srno)
        post=Posts.query.filter_by(srno=srno).first()
        return render_template('edit.html',params=params,post=post,srno=srno)

@app.route('/uploader',methods=['GET','POST'])
def uploader():
    if ('user' in session and session['user']==params['admin_user']):
        if request.method=="POST":
            f=request.files['file1']
            f.save(os.path.join(app.config['UPLOAD_FOLDER'],secure_filename(f.filename)))
            return "Uploaded Sucessfully"

@app.route('/logout',methods=['GET','POST'])
def logout():
    session.pop('user')
    return redirect('/dashboard')

@app.route('/delete/<string:srno>',methods=['GET','POST'])
def delete(srno):
    if ('user' in session and session['user']==params['admin_user']):
        post=Posts.query.filter_by(srno=srno).first()
        db.session.delete(post)
        db.session.commit()
    return redirect('/dashboard')

if __name__ =='__main__':
    app.run(debug=True)

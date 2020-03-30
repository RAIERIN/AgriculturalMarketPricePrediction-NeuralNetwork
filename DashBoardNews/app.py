from flask import Flask, render_template, flash, redirect, url_for, session, logging, request, session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import select,insert
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt
from functools import wraps
from sqlalchemy.orm.attributes import flag_modified
import datetime
current_date = datetime.date.today()

app = Flask(__name__)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://erin:admin@localhost/agroprediction'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email_id = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

    def __init__(self,username,email_id, password):
        self.username = username
        self.email_id = email_id
        self.password = password

    def __repr__(self):
        return '<User %r>'%self.id
class News(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), unique=True, nullable=False)
    author = db.Column(db.String(100), nullable=False)
    body = db.Column(db.Text, unique=True, nullable=False)
    create_date = db.Column(db.Date, nullable=False)

    def __init__(self,title,author, body, create_date):
        self.title = title
        self.author = author
        self.body = body
        self.create_date = create_date

#index
@app.route('/')
def index():
    return render_template('home.html')

#Register form
class RegisterForm(Form):
    username = StringField('Name',  [validators.Length(min=1, max=100)])
    email_id = StringField('Email', [validators.Length(min=10, max=100)])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Password do not match!')
    ])
    confirm = PasswordField('Confirm Password')

#User register
@app.route('/register',methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        username = str(form.username.data)
        email_id = str(form.email_id.data)
        password = str(sha256_crypt.encrypt(str(form.password.data)))
        print(username)
        print(email_id)
        print(password)
        user = User(username,email_id,password)
        db.session.add(user)
        db.session.commit()
        flash('You are now registered and can login', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

#User login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if  request.method == 'POST':
        #Get form fields
        username = request.form['username']
        password_candidate = request.form['password']

        #database query
        result = db.session.query(User.username, User.password).filter(User.username==username)
        app.logger.info(result)
        output = []
        for row in result:
            output.append(row)
        app.logger.info(output)
        if output:
            vals = {}
            for userdetail in output:
                vals['username']=userdetail[0]
                vals['password']=userdetail[1]
            #compare password
            password = vals['password']
            if sha256_crypt.verify(password_candidate, password):
                #Passed
                session['logged_in'] = True
                session['username'] = vals['username']

                flash('You are now logged in', 'success')
                return redirect(url_for('dashboard'))
            else:
                error = 'Password Incorrect'
                return render_template('login.html', error=error)
        else:
            error = 'Username not found'
            return render_template('login.html', error=error)
    return render_template('login.html')

# Check if user logged in
def is_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('Unauthorized, Please login', 'danger')
            return redirect(url_for('login'))
    return wrap

#Logout
@app.route('/logout')
@is_logged_in
def logout():
    session.clear()
    flash('You are now logged out', 'success')
    return redirect(url_for('login'))

#Dashboard
@app.route('/dashboard')
@is_logged_in
def dashboard():
    data = News.query.all()
    app.logger.info(data)
    if data:
        news = []
        for new in data:
            vals = {}
            vals['id']=new.id
            vals['title']=new.title
            vals['author']=new.author
            vals['body']=new.body
            vals['current_date']=new.create_date
            news.append(vals)

        app.logger.info(news)
        return render_template('dashboard.html', news = news)
    else:
        msg='No News found'
    return render_template('dashboard.html')

#News form Class
class NewsForm(Form):
    title = StringField('Title',  [validators.Length(min=1, max=200)])
    body = TextAreaField('Body', [validators.Length(min=30)])
#Add news
@app.route('/add_news', methods=['GET', 'POST'])
@is_logged_in
def add_news():
    form = NewsForm(request.form)
    if request.method == 'POST' and form.validate():
        title = form.title.data
        body = form.body.data
        author = session['username']
        news = News(title,author,body,current_date)
        db.session.add(news)
        db.session.commit()
        flash('News Created','success')
        return redirect(url_for('dashboard'))
    return render_template('add_news.html',form=form)

#Edit News
@app.route('/edit_news/<string:id>', methods=['GET','POST'])
@is_logged_in
def edit_news(id):
    form = NewsForm(request.form)
    if request.method == 'POST' and form.validate():
        title=form.title.data
        body=form.body.data

        upd = db.session.query(News).filter_by(id=id).first()  # @note: code is Integer, not a String, right?
        if upd:
            upd.title = title
            upd.body = body
            db.session.add(upd)
            db.session.commit()
        flash('News Updated', 'Success')
        return redirect(url_for('dashboard'))
    return render_template('edit_news.html',form=form)

#Delete News
@app.route('/delete_news/<string:id>', methods=['POST'])
@is_logged_in
def delete_news(id):
    data = db.session.query(News).filter_by(id=id).first()
    db.session.delete(data)
    db.session.commit()
    flash('News Deleted', 'success')
    return redirect(url_for('dashboard'))
if __name__=='__main__':
    app.secret_key='secret123'
    app.run(debug=True,port=80)

from flaskBlog import app
from flask import render_template
from flaskBlog.forms import RegistrationForm,LoginForm
from flask import flash
from flask import url_for,redirect
from flaskBlog.models import User
from flaskBlog import bcrypt,db
@app.route('/')
def home():
    posts =[{"title":"1st post","Description":"1st Description"},
            {"title":"2nd post","Description":"2nd Description"}]
    return render_template('index.html',posts=posts)

@app.route('/about')
def about():
    return render_template('about.html',title='About')

@app.route('/register',methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password=bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data,email=form.email.data,
                    password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Account Created for {user.username}','success')
        return redirect(url_for('login'))
    return render_template('register.html',title='Register',form=form)


@app.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'User logged in','success')
    return render_template('login.html',title='Sign In',form=form)
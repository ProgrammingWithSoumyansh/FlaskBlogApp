from flaskBlog import app
from flask import render_template
from flaskBlog.forms import RegistrationForm,LoginForm
from flask import flash
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
        flash(f'User Created','success')
    return render_template('register.html',title='Register',form=form)


@app.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'User logged in','success')
    return render_template('login.html',title='Sign In',form=form)
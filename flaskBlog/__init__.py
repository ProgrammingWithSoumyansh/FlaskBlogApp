from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY']='mysecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///database.db'
db= SQLAlchemy(app)
bcrypt=Bcrypt(app)
login_manager = LoginManager(app)
from flaskBlog import routes
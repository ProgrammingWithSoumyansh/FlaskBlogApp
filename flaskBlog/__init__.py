from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SECRET_KEY']='mysecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///database.db'
db= SQLAlchemy(app)
bcrypt=Bcrypt(app)
from flaskBlog import routes
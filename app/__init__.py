from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Sup3r$3cretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://lrxskdxxgryumx:3e673130d16090f8df0998db34654ad8b17c67a181c3b8f28f074a0335ca451c@ec2-107-20-233-240.compute-1.amazonaws.com:5432/dfjeo3c1tv9af'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning
app.config['UPLOAD_FOLDER'] = "./app/static/uploads"

db = SQLAlchemy(app)


app.config.from_object(__name__)
from app import views


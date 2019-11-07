from flask import Flask, request, redirect, url_for, Response
from flask_sqlalchemy import SQLAlchemy
from flask_sqlalchemy.model import Model

dbdir = 'sqlite:////databae/database.db'
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = dbdir
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from database import Model
db.create_all()

@app.route('/index')
def index():
    return redirect(url_for('/login'))

@app.route('/login', methods=['GET','POST'])
def login(userdata):
  pass



if __name__ == "__main__":
    db.create_all()
    app.run(
        port=5000,
        debug=True
    )
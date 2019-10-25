from flask import Flask, request, redirect, url_for, jsonify
from sqlalchemy import Column, Date, DateTime, Float, String, TIMESTAMP
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.ext.declarative import declarative_base



app = Flask(__name__)
db = SQLAlchemy(app)

from database.Models import Usuario, Role, 

@app.route('/')
def index():
    return redirect(url_for('/login'))

@app.route("/signup", methods=['GET', 'POST'])
def register(data):
    if request.methods =='GET':
        new_request = Usuario()
        modelo = {
            new_request.Name: request.form['name'],
            new_request.LastName: request.form['lastname'],
            new_request.Rut: request.form['rut'],
            new_request

        }



@app.route('/login', methods= ['GET, POST'])
def login(data):





if __name__ == "__main__":
    db.create_all()
    app.run(port=5000,debug=True)
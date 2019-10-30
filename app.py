import os
from flask import Flask, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:powermetal.4@localhost/final'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# RUTAS
@app.route('/')
def index():
    return redirect(url_for('/login'))


# Ruta-login
@app.route('/login', methods=['POST'])
def login(username, password):
    return jsonify("todo ok")

@app.route('/dashboard', methods=['GET'])
def dashboard():
    pass

db.create_all()
if __name__ == "__main__":
    app.run(port=5000,
            debug=True)

import os
from flask import Flask, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:powermetal.4@localhost/final'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app = Flask(__name__)
db = SQLAlchemy()
def create_app():
    db.init_app(app)
    return app

from db import Models
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


if __name__ == "__main__":
    app.run(port=5000,
            debug=True)

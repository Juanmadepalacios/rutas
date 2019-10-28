from flask import Flask, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

direccion = os.path.abspath(os.getcwd())+"db/modelo.db"
url = 'sqlite:///'+direccion
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = url

db = SQLAlchemy(app)
from db import Models
# RUTAS
@app.route('/')
def index():
    return redirect(url_for('/login'))


# Ruta-login
@app.route('/login', methods=['POST'])
def login():
    return jsonify("todo ok")


if __name__ == "__main__":
    app.run(port=5000,
            debug=True)

from flask import Flask, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']=url
app.comfig['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db = SQLAlchemy(app)

from db.database.Models import Usuario

#RUTAS
@app.route('/')
def index():
    return redirect(url_for('/login'))

import routers




if __name__ == "__main__":
    db.create_all()
    app.run(port=5000,debug=True)
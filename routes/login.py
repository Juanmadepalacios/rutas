from db.Models import Usuario
from flask import request
from app import app
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    new_login = Usuario()
    if request.methods == 'POST':
        new_login.username = request.form['username']
        new_login.password = request.form['password']


        if new_login.username and new_login.password:

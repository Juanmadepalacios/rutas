from flask import Flask, request, redirect, url_for
from flask_mysqldb import MySQL
from person import User
app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'powermetal.4'
app.config['MYSQL_DB'] = 'final'

mysql = MySQL(app)

usuario = User()

app.secret_key = 'hololololo'


@app.route('/')
def hello_world():
    return redirect(url_for('/login'))


@app.route('/login', methods=['POST'])
def login(data):
    if request == 'POST':
        data.username = request.form['username']
        data.password = request.form['password']
    return usuario.login(data)


if __name__ == '__main__':
    app.run(port=5000, debug=True)

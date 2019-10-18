from flask import Flask, request, redirect, url_for, jsonify
from

app = Flask(__name__)







@app.route('/')
def hello_world():
    return redirect(url_for('/login'))


@app.route('/login', methods=['POST'])
def login(data):


@app.route('/user/<int: id>')
def register():





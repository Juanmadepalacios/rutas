from app import *

@app.route('/')
def index():
    return redirect(url_for('/login'))


@app.route('/login', methods=['GET, POST'])
def login (self, data):

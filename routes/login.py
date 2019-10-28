from db.Models import Usuario
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.methods=='POST':
        if valid_login(request.form['username'],
                        request.form['password']):
                        new_login = Usuario()
                        
from db.Models import Usuario
from flask import request
from app import db, app


@app.route('/registro', methods=['POST'])
def registry():
    new_user = Usuario()
    new_user.name = request.form['name']
    new_user.last_name = request.form['lastname']
    new_user.rut = request.form['rut']
    new_user.dV = request.form['verificador']
    new_user.mail = request.form['email']
    new_user.username = request.form['username']
    new_user.password = request.form['password']
    new_user.image = request.form['thumbnail']

    if new_user:

        new_user.name.capitalize()
        new_user.last_name.capitalize()
        new_user.dv.upper()

        insertion = db.session.add(new_user.Name,
                                   new_user.last_Name,
                                   new_user.rut,
                                   new_user.dV,
                                   new_user.mail,
                                   new_user.username,
                                   new_user.password,
                                   new_user.image)
        if insertion:
            db.session.commit()




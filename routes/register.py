from db.Models import Usuario
from flask import request, Response
from flask import jsonify
from app import db, app
import re
import rut_chile

@app.route('/registro', methods=['POST'])
def registry():
    bodydata = request.get_json()
    new_user = Usuario()
    persona = {
        "name": bodydata['name'],
        "lastname": bodydata['lastname'],
        "rut": bodydata['rut'],
        "verifcador": bodydata['verificador'],
        "email": bodydata['email'],
        "username": bodydata['username'],
        "password": bodydata['password'],
        "thumbnail": bodydata['thumbnail']
    }
    respuesta= persona + Response.status_code
    if bodydata is True:
        new_user.name = persona["name"]
        if (20 >= len(new_user.name) >= 5) and new_user.name:
            new_user.name.capitalize()
            new_user.last_name = persona["lastname"]
            if (20 <= len(new_user.last_name) >= 5) and new_user.last_name:
                new_user.last_name.capitalize()
                new_user.rut = persona["rut"]
                if rut_chile.is_valid_rut(new_user.rut):
                    new_user.persona["verificador"]
                    if rut_chile.get_verifiction_digit(new_user.rut) == new_user.dv:
                        new_user.mail = persona["email"]
                        if re.match('^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)][(a-z)]{2,15}$', new_user.mail.lower()):
                            new_user.username = persona["username"]
                            if (10 >= len(new_user.username) <=12):
                                new_user.password = persona["password"]
                                if re.match('^[(a-z0-9A-Z\_\-\.)]', new_user.password):

                            else:
                                jsonify("el correo exede o le faltan la cantidad de carateres permitidos")
                        else:
                            jsonify("favor validar el formato del correo electronico").Response.status_code=406
                    else:
                        jsonify(" favor validar que el digito verificador sea correcto ")
                else:
                    jsonify("rut invalido")
            else:
                return jsonify("validar cantdad de caracteres del apellido").Response
        else:
            return jsonify("validar largo de caracteres para usuario")

    new_user.name = request.json['name']
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

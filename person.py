from flask import jsonify, redirect, url_for
import db.dbconnection
from app import mysql


class User:
    def __init__(self, first_name, last_name, username, birthday, rut, dv, image,
                 mail, password, estado):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.birthday = birthday
        self.rut = rut
        self.dv = dv
        self.image = image
        self.mail = mail
        self.password = password
        self.estado = estado

    def state(self):
        return self.estado
    def register_user(self, userdata):
        data = [{
            userdata['first_name']: self.first_name,
            userdata['last_name']: self.last_name,
            userdata['username']: self.username,
            userdata['birthday']: self.birthday,
            userdata['rut']: self.rut,
            userdata['dv']: self.dv,
            userdata['image']: self.image,
            userdata['mail']: self.mail,
            userdata['password']: self.password,
            userdata['estado']: "REGISTRADO"
        }]
        cur = mysql.connection.cursor()
        qmark = ','.join('?'*len(data))
        cur.execute('INSERT INTO final.usuario (first_name, last_name, '
                    'birthdate, rut, dv, username, ImagePerfil, '
                    'mail, password, creation_date, estado) '
                    'values (%s, %s, %s, %s, %s, %s , %s, %s, %s, %s, %s), '
                    '(First_Name, Last_Name, BirthDate, Rut, DV, username,'
                    'ImagePerfil, mail, password, creation_date, Estado )')
        if cur:
            return redirect(url_for,)
        else:
            return "favor validar informacion"
    def login(self, logindata):
        self.username = logindata
        self.password = logindata
        cur = mysql.connection.cursor()
        cur.execute('SELECT username, password FROM final.usuario '
                    'WHERE username = %s AND password = %s ')
        if cur:
            return True
        else:
            return jsonify("datos incorretos favor verificar")


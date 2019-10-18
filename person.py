from flask import jsonify, redirect, url_for
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


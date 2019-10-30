#database Relacional SQLALCHEMY
from app import db
from app import SQLAlchemy
from app import create_app
from flask_sqlalchemy import Model, dec



class Usuario(db.Model):
    __tablename__='usuarios'
    id = db.Column(db.Integer, primary_key=True, nullable=False, unique =True)
    name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(20), nullable=False)
    rut = db.Column(db.Integer, nullable=False)
    dv = db.Column(db.String(1), nullable=False)
    mail = db.Column(db.String(20), nullable=False)
    username = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(20), nullable=False)
    image = db.Column(db.LargeBinary(20), nullable=True)
    # Foreigns Keys
    rol_id = db.Column(db.ForeignKey('Rol.id'), nullable=False)

    def __repr__(self):
        return '<usuario %r>' % self.name, self.last_name, self.rut, self.dv, self.mail, self.username, self.password, self.image, self.rol_id
    
    def serialize(self):
        return {
            "id":self.id,
            "name": self.name,
            "last_name": self.last_name,
            "rut": self.rut,
            "dv": self.dv,
            "mail": self.mail,
            "username": self.username,
            "password": self.password,
            "image": self.image,
            "rol_id": self.rol_id
        }

class Sesion(db.Model):
    __tablename__='sesion'
    id = db.Column(db.Integer, primary_key=True, nullable=False, unique = True)
    user = db.Column(db.String(50), nullable=False)
    rol = db.Column(db.String(20), nullable=False)
    session_start = db.Column(db.DateTime, nullable=False)
    session_close = db.Column(db.DateTime, nullable=True)
    # ForeignKeys
    user_id = db.Column(db.ForeignKey('Usuario.id'), nullable=False)

    def __repr__(self):
        return '<sesion %r>' % self.id, self.user, self.rol, self.session_start, self.session_close, self.user_id
    
    def serialize(self):
        return{
            "id": self.id,
            "user": self.user,
            "rol": self.rol,
            "session_start": self.session_start,
            "session_close": self.session_close
        }

class Rol(db.Model):
    __tablename__='roles'
    id = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
    role_name = db.Column(db.String, nullable=False)

    def __repr__(self):
        return '<Rol %r>' % self.id, self.role_name
    
    def serialize(self):
        return {
            "id": self.id,
            "role_name": self.role_name
        }

class Tarea(db.Model):
    __tablename__='tareas'
    id = db.Column(db.Integer, primary_key=True, nullable=False, unique = True)
    user_id = db.Column(db.Integer, db.ForeignKey('Usuario.id'), nullable=False)
    description = db.Column(db.String(150), nullable=False)
    creation = db.Column(db.DateTime, nullable=False)
    price = db.Column(db.Float, nullable=False)
    category = db.Column(db.Integer, db.ForeignKey('Categoria.id'), nullable=False)
    status = db.Column(db.String(10), nullable=False)

    def __repr__(self):
        return '<Tarea %r>' % self.id, self.User_id, self.Description, self.Creation, self.Price, self.Category, self.Status

    def sererialize(self):
        return{
            "id": self.id,
            "user_id": self.user_id,
            "description": self.description,
            "creation": self.creation,
            "price": self.price,
            "category":self.category,
            "status": self.status
        }

class Categoria(db.Model):
    __tablename__='categorias'
    id = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
    name = db.Column(db.String(20), nullable=False)
    code = db.Colum(db.String(20), nullable=False, unique=True)

    def __repr__(self):
        return '<Categoria %r>' % self.id, self.Category_name
    def serialize(self):
        return{
            "id": self.id,
            "category_name": self.category_name
        }

class Solicitud_Tarea(db.Model):
    __tablename__='solcitud_tarea'
    id = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
    tarea_id = db.Column(db.Integer, db.ForeignKey('Tarea.id'), nullable=False)
    comentary = db.Column(db.String(150), nullable=False)
    new_price = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return '<Solicitud_Tarea %r>' % self.id, self.tarea_id, self.comentary, self.new_price, self.status
    def sererialize(self):
        return{
            "id": self.id,
            "tarea_id": self.tarea_id,
            "comentary": self.comentary,
            "new_price": self.new_price,
            "status": self.status
        }
class Candidato(db.Model):
    __tablename__='candidatos'
    id = db.Column(db.Integer, primary_key = True, unique = True)
    task_id = db.Column(db.Integer, db.Foreign_key('Tarea.id'), nullable = False)
    user_service_id = db.Column(db.Integer, db.Foreign_key('Usuario.id'), nullable= False)
    status = db.Column(db.String(10), nullable=False)
    def __repr__(self):
        return '<Candidato %r>' % self.id, self.task_id, self.user_service_id, self.status 
    def serialize(self):
        return{
            "id": self.id,
            "task_id": self.task_id,
            "user_service_id": self.user_service_id,
            "status": self.status
        }
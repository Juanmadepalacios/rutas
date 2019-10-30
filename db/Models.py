# database Relacional SQLALCHEMY

from app import db
import datetime


class Profile(db.Model):
    __tablename__ = 'profile'
    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    name = db.Column(db.String(20), nullable=False)
    lastname = db.Column(db.String(20), nullable=False)
    rut = db.Column(db.Integer, nullable=False)
    dv = db.Column(db.String(1), nullable=False)

    def __repr__(self):
        return '<profile %r>' % self.id, self.name, self.lastname, self.rut, self.dv

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "lastname": self.lastname,
            "rut": self.rut,
            "dv": self.dv
        }


class Rol(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
    name = db.Column(db.String(12), nullable=False)
    code = db.Column(db.String(10), nullable=False, unique=True)

    def __repr__(self):
        return '<roles %r>' % self.id, self.name, self.code

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "code": self.code
        }


class Usuario(db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey('profile.id'), nullable=False)
    mail = db.Column(db.String(20), nullable=False)
    username = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(20), nullable=False)
    image = db.Column(db.LargeBinary(20), nullable=True)
    # Foreigns Keys
    rol_id = db.Column(db.Integer, db.ForeignKey('roles.id'), nullable=False)

    def __repr__(self):
        return '<usuario %r>' % self.id, self.user_id, self.mail, self.username, self.password, self.image, self.rol_id

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "mail": self.mail,
            "username": self.username,
            "password": self.password,
            "image": self.image,
            "rol_id": self.rol_id
        }


class Sesion(db.Model):
    __tablename__ = 'sesion'
    id = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
    user_id = db.Column(db.Integer(50), db.ForeignKey('usuarios.id'), nullable=False)
    session_start = db.Column(db.DateTime, nullable=False)
    session_close = db.Column(db.DateTime, nullable=True)

    def __repr__(self):
        return '<sesion %r>' % self.id, self.user, self.user_id, self.session_start, self.session_close

    def serialize(self):
        return {
            "id": self.id,
            "user": self.user,
            "user_id": self.user_id,
            "session_start": self.session_start,
            "session_close": self.session_close
        }


class Tarea(db.Model):
    __tablename__ = 'tareas'
    id = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
    title = db.Column(db.String(20), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('Usuario.id'), nullable=False)
    description = db.Column(db.String(150), nullable=False)
    creation = db.Column(db.DateTime, nullable=False)
    end = db.Column(db.Time, nullable=False)
    price = db.Column(db.Float, nullable=False)
    category = db.Column(db.Integer, db.ForeignKey('Categorias.id'), nullable=False)
    status = db.Column(db.String(10), nullable=False)

    def __repr__(self):
        return '<Tarea %r>' % self.id, self.User_id, self.Description, self.Creation, self.Price, self.Category, self.Status

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "description": self.description,
            "creation": self.creation,
            "price": self.price,
            "category": self.category,
            "status": self.status
        }


class Categoria(db.Model):
    __tablename__ = 'categorias'
    id = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
    name = db.Column(db.String(20), nullable=False)
    code = db.Colum(db.String(20), nullable=False, unique=True)

    def __repr__(self):
        return '<Categoria %r>' % self.id, self.Category_name, self.code

    def serialize(self):
        return {
            "id": self.id,
            "category_name": self.category_name,
            "code": self.code
        }


class Solicitud_Tarea(db.Model):
    __tablename__ = 'solcitud_tarea'
    id = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
    tarea_id = db.Column(db.Integer, db.ForeignKey('Tarea.id'), nullable=False)
    user_service_id = db.Column(db.Integer, db.foreign_key('Usuario.id'), nullable=False)
    comentary = db.Column(db.String(150), nullable=False)
    status = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return '<Solicitud_Tarea %r>' % self.id, self.tarea_id, self.user_service_id, self.comentary, self.status

    def sererialize(self):
        return {
            "id": self.id,
            "tarea_id": self.tarea_id,
            "user_service_id": self.user_service_id,
            "comentary": self.comentary,
            "status": self.status
        }

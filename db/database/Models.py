from flask_sqlalchemy import SQLAlchemy

class Usuario(db.Model):
    id = eb.Column(db.Integer, primary_key=True, nullable=False, unique =True)
    Name = db.Column(db.String(50), nullable=False)
    Last_name = Column(String(50), nullable=False)
    Rut = db.Column(db.Integer, nullable=False)
    Dv = db.Column(db.String(1), nullable=False)
    Mail = db.Column(db.String(50), nullable=False)
    Username = db.Column(db.String(20), nullable=False)
    Password = db.Column(db.String(20), nullable=False)
    Image = db.Column(db.LargeBitmap(50), nullable=True)
    # Foreigns Keys
    Rol_id = db.Column(db.ForeignKey('Roles.id'), nullable=False)

    def __repr__(self):
        return '<usuario %r>' % self.Name, self.Last_name, self.Rut, self.Dv, self.Mail, self.Username, self.Password, self.Image, self.Rol_id


class Sesion(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False, unique = True)
    User = db.Column(db.String(50), nullable=False)
    Rol = db.Column(db.String(20), nullable=False)
    Session_start = db.Column(db.DateTime, nullable=False)
    Session_close = db.Column(db.DateTime, nullable=True)
    # ForeignKeys
    User_id = db.Column(db.ForeignKey('Usuario.id'), nullable=False)

    def __repr__(self):
        return '<sesion %r>' % self.id, self.User, self.Rol, self.Session_start, self.Session_close, self.User_id

class Roles(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False unique=True)
    Role_name = db.Column(db.String, nullable=False)

    def __repr__(self):
        return '<Roles %r>' % self.id, self.Role_name


class Tarea(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False, unique = True)
    User_id = db.Column(db.Integer, db.ForeignKey('Usuario.id'), nullable=False)
    Description = db.Column(db.String(150), nullable=False)
    Creation = db.Column(db.DateTime, nullable=False)
    Price = db.Column(db.Float, nullable=False)
    Category = db.Column(db.Integer, db.ForeignKey('Categoria.id'), nullable=False)
    Status = db.Column(db.String(10), nullable=False)

    def __repr__(self):
        return '<Tarea %r>' % self.id, self.User_id, self.Description, self.Creation, self.Price, self.Category, self.Status


class Categoria(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
    Category_name = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return '<Categoria %r>' % self.id, self.Category_name


class Solicitud_Tarea(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    Tarea_id = db.Column(db.Integer, db.ForeignKey('Tarea.id'), nullable=False)
    Comentary = db.Column(db.String(150), nullable=False)
    new_price = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return '<Solicitud_Tarea %r>' % self.id, self.Tarea_id, self.Comentary, self.new_price, self.status


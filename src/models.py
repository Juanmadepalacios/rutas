from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    username = db.Column(db.String(20), nullable =False)
    password = db.Column(db.String(20), nullable =False)
    mail = db.Column(db.String(20), nullable = False)
    phone = db.Column(db.Integer, nullable = False)
    image = db.Column(db.LargeBinary, nullable = False)

    #Relationship
    profile_id= db.Column(db.Integer, db.ForeignKey('profile.id'), nullable=False)
    profile = db.relationship('Profile', backref = db.backref('profile', lazy=True))

    rol_id = db.Column(db.Integer, db.ForeignKey('rol.id'), nullable=False)
    rol = db.relationship('Rol', backref = db.backref('rol', lazy=True))
    def __repr__(self):
        return '<User %r>' % self.username
    
    def serialize(self):
        return {
            "username": self.username,
            "password": self.password,
            "mail": self.mail,
            "phone": self.phone,
            "profile": self.profile_id,
            "rol": self.rol_id
        }

class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable = False)
    lastname = db.Column(db.String(20), nullable = False)
    rut = db.Column(db.String(15), nullable = False)

    def __repr__(self):
        return '<Profile %r>' % self.name
    
    def serialize(self):
        return {
            "name": self.name,
            "lastname": self.lastname,
            "rut": self.rut
        }

class Rol(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10), nullable = False)
    code = db.Column(db.String(20), nullable = False )

    def __repr__(self):
        return '<Rol %r>' % self.name

    def serialize(self):
        return{
            "name": self.name,
            "code": self.code
        }
class Task(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    title = db.Column(db.String(25), nullable = False)
    commentary = db.Column(db.String(150), nullable= False)
    creation = db.Column(db.DateTime, nullable = False)
    start =db.Column(db.DateTime, nullable = False)
    final = db.Column(db.DateTime, nullable = True) 
    price = db.Column(db.Float, nullable = False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    region_id = db.Column(db.Integer, db.ForeignKey('region.id'), nullable=False)
    Comunne_id = db.Column(db.Integer, db.ForeignKey('comunne.id'), nullable=False)
    code = db.Column(db.String(10), nullable = False, unique = True)
    status = db.Column(db.String(10), nullable=False)
    # Outside Columns
    region = db.relationship('Region', backref= db.backref('region', lazy=True))
    comunne = db.relationship('Comunne', backref = db.backref('comunne', lazy=True))
    category = db.relationship('Category', backref = db.backref('category', lazy=True))

    def __repr__(self):
        return '<Task %r>' % self.title
    def serialize(self):
        return{
            "title": self.id,
            "commentary":self.commentary,
            "date": self.date,
            "price": self.price,
            "category": self.category,
            "region": self.region_id,
            "commune": self.Comunne_id,
            "status": self.status 
        }
class Region(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25), nullable = False)
    code = db.Column(db.String(10), nullable = False, unique = True)

    def __repr__(self):
        return '<Region %r>' % self.name
    
    def serialize(self):
        return{
            "name": self.name,
            "code": self.code
        }
class Comunne(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(20), nullable = False)
    code = db.Column(db.String(20), nullable = False, unique = True)

    def __repr__(self):
       return '<Comunne %r>' % self.name

    def serialize(self):
        return{
            "name": self.name,
            "code": self.code
        }
class Category(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(10), nullable = False)
    code = db.Column(db.String(10), nullable = False, unique = True)

    def __repr__(self):
        return '<Category %r>' % self.name
    
    def serialize(self):
        return{
            "name": self.name,
            "code": self.code
        }
    
class Request(db.Model):
    id = db.Column(db.Integer, primary_key = True, unique = True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
    task_id = db.Column(db.Integer, db.ForeignKey('task.id'), nullable = False)
    commentary = db.Column(db.String(150), nullable = False)
    status = db.Column(db.String(10), nullable = False)
    
    #relationship
    task = db.relationship('Task', backref= db.backref('task', lazy=True))
    user = db.relationship('User', backref= db.backref('user', lazy=True))

    def __repr__(self):
        return '<Request %r>' % self.task_id

    def serialize(self):
        return {
            "task_id": self.task_id,
            "commmentary": self.commentary,
            "status": self.commentary
        }

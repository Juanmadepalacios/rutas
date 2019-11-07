

class Usuario(db.Model):
    id  =  db.Column(db.Integer, Primary_Key=True, nulleable=False)
    Name = db.Column(db.String(50), nulleable=False)
    Last_name = db.Column(db.String(50), nulleable=False)
    Rut = db.Column(db.Integer, nulleable=False)
    Dv = db.Column(db.String(1), nulleable=False)
    Mail = db.Column(db.String(50), nulleable=False)
    State_comuna = db.Column(db.String(50), nulleable=False)
    Contact = db.Column(db.Integer, nulleable= False)
    Image = db.Column(db.String(50), nulleable=True)
    #Foreigns Keys
    rol_id = db.Column(db.ForeignKey('Roles.id'), nulleable=False)


    def __repr__(self):
        return '<usuario %r>' % self.name,
        self.last_name,
        self.rut,
        self.dv,
        self.mail,
        self.state_comuna,
        self.contact,
        self.image


class Sesion(db.Model):
    id = db.Column(db.Integer, Primary_key=True, nulleable=False)
    User = db.Column(db.String(50), nulleable=False)
    rol = db.Column(db.String(20), nulleable=False)
    sesion_start= db.Column(db.DateTime, nulleable=False, default=datetime.utcnow)
    Session_close = db.Column(db.DateTime, nulleable=True)
    #ForeignKeys
    user_id = db.Column(db.ForeignKey('Usuario.id'), nulleable=False)
    def __repr__(self):
        return '<sesion %r>' % self.id,
        self.User,
        self.rol,
        self.sesion_start,
        self.Session_close

class Roles(db.Model):
    id = db.Column(db.Integer, Primary_key=True, nulleable=False)
    Role_name = db.Column(db.String, nulleable=False)

    def __repr__(self):
        return '<Roles %r>' % self.id,
        self.Role_name

class Tarea(db.Model):
    id = db.Column(db.Integer,Primary_key=True, nulleable=False)
    User_id = db.Column(db.Integer, db.ForeignKey('Usuario.id'), nulleable=False)
    Description = db.Column(db.String(150), nulleable=False)
    Creation = db.Column(db.DateTime, nulleable = False, default=datetime.utcnow)
    Price =db.Column(db.Float, nulleable=False)
    Category = db.Column(db.Integer, db.ForeignKey('Categoria.id'), nulleable=False)
    Status = db.Column(db.String(10), nulleable = False)

    def __repr__(self):
        return '<Tarea %r>' % self.id,
        self.User_id,
        self.Description,
        self.Creation,
        self.Price,
        self.Category,
        self.Status

class Categoria(db.Model):
    id = db.Column(db.Integer, Primary_key=True, nulleable = False)
    Category_name = db.Column(db.String(20), nulleable=False)

    def __repr__(self):
        return '<Categoria %r>' % self.id, self.Category_name

class Solicitud_tarea(db.Model):
    id = db.Column(db.Integer, Primary_key=True, nulleable=False)
    Tarea_id = db.Column(db.Integer,db.ForeignKey('Tarea.id'), nulleable=False)
    Comentary = db.Column(db.String(150), nulleable=False)
    new_price = db.Column(db.Float, nulleable=False)
    status = db.Column(db.String(20), nulleable=False)

    def __repr__(self):
        return '<Solicitud_Tarea %r>' % self.id,
        self.Tarea_id,
        self.Comentary,
        self.new_price,
        self.status




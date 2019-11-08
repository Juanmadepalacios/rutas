from src.models import User, Rol, Profile, db
from src.main import app, request
from werkzeug.security import generate_password_hash

@app.route('/registro', methods=['POST'])
def register():
        if request.method == 'POST':
            data = request.get_json()
            print(data)
            hashed_pw = generate_password_hash(data["password"], method='sha256')
            new_user = User(
                username=data["username"],
                password=hashed_pw,
                mail=data["mail"],
                phone=data["phone"],
                image=data["image"]
            )
            new_profile = Profile(
                name=data["name"],
                lastname=data["lastname"],
                rut=data["rut"]
            )
            new_rol = Rol(
                name="User",
                code="codigo1"
            )
            new_user.rol = new_rol
            new_user.profile = new_profile
            db.session.add(new_user)
            if db:
                db.session.commit()
                return "new user data succefully inserted"
            else:
                return "esta wea se rompio"
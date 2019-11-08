from src.models import User
from src.main import app, request, jsonify
from passlib.hash import pbkdf2_sha256 as sha256
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token, create_refresh_token,
    get_jwt_identity
)

@app.route('/login')
def signup():
    data = request.json
    user = User.query.filter_by(username=data["username"]).first()
    if user is None:
        return jsonify({
            "error": "el usuario no existe"
        }), 404
    if sha256.verify(data["password"], user.password):
        tocken = create_access_token(identity=data["username"])
        refresh = create_refresh_token(identity=data["username"])

        return jsonify({
            "token": tocken,
            "refresh": refresh
        }), 200

    return jsonify({
        "error": "la contraseña no es valida"
    }), 404

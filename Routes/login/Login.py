from src.models import User
from src.main import app, request, jsonify
from passlib.hash import pbkdf2_sha256 as sha256


@app.route('/login')
def signup():
    data = request.json
    user = User.query.filter_by(username=data["username"]).first()
    if user is None:
        return jsonify({
            "error": "el usuario no existe"
        }), 404
    if sha256.verify(data["password"], user.password):
        mivariable = create_access_token(identity=data["username"])
        refresh = create_refresh_token(identity=data["username"])
        return jsonify({
            "token": mivariable,
            "refresh": refresh
        }), 200

    return jsonify({
        "error": "la contraseña no es valida"
    }), 404

@app.route('/registro', methods=['POST'])
def registro():
    nuevo_usuario = Usuario()
    nuevo_usuario.name = request.form['name']
    nuevo_usuario.last_name = request.form['lastname']
    nuevo_usuario.rut = request.form['rut']
    nuevo_usuario.dV = request.form['verificador']
    nuevo_usuario.mail = request.form['email']
    nuevo_usuario.username = request.form['username']
    nuevo_usuario.password = request.form['password']
    nuevo_usuario.image = request.form['thumbnail']

    nuevo_usuario.name.capitalize()
    nuevo_usuario.last_name.capitalize()
    nuevo_usuario.dv.upper()

    insertion = db.session.add(nuevo_usuario.Name,
    nuevo_usuario.last_Name,
    nuevo_usuario.rut,
    nuevo_usuario.dV,
    nuevo_usuario.mail,
    nuevo_usuario.username,
    nuevo_usuario.password,
    nuevo_usuario.image)

    if insertion:
        return jsonify(
            "insertado correctamente"
        )
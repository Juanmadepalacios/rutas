from db.Models import Tarea
from flask import jsonify, request
from app import app


@app.route('/tareas', methods=['GET'])
def listartareas():
    getTareas = Tarea()
    lista = getTareas.query.filter(status='Disponible').all()
    if lista:
        return jsonify(lista=lista)
    else:
        return jsonify(lista=None)

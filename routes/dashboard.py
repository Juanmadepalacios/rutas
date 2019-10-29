from flask import request
from db.Models import Categoria
from app import app
from app import db


@app.route('/categoria/', methods=['GET'])
def categoria_uno(name):
    name = request.form['']
    categoria = Categoria()
    categoria.query.filter(
        categoria.category_name
    )
@app.route('/categoria/<subdomain :string>')

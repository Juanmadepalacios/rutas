from db.Models import Tarea, Categoria
from app import app

@app.route('/tareas/<string:categories>', methods=['GET'])
def getcategories(categories):
    listarcategorias = Tarea()
    listar = listarcategorias.query.filter_by(category = getcategories,
                                              status = 'Disponible').all()
    if listar:

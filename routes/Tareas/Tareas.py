from app import db, app
from db.Models import Tarea

@app.route('/Tareas', methods=['GET'])
def tareas(): 
    from routes.Tareas import task_request


@app.route('/Tareas/<int: id>', methods =['GET'])
def listaTareas(id):
    pass

@app.route('/Tareas/<String: categoria>/<int: id>', methods=['GET', 'POST'])
def Categoriatareas(categoria, id):
    pass
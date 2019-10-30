from app import db, app
from db.Models import Tareas
from db.Models import Usuario, Tarea
import datetime

@app.route('/Tareas', methods=['GET', 'POST'])
def tareas(): 

   


@app.route('/Tareas/<int: id>', methods =['GET'])
def listaTareas(id):
    pass

@app.route('/Tareas/<String: categoria>/<int: id>', methods=['GET', 'POST'])
def Categoriatareas(categoria, id):
    pass
from app import db, app
from db.Models import Tareas

@app.route('/Tareas', methods=['GET', 'POST'])
def tareas(solicitud, id):
    Tareas 
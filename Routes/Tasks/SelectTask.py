from src.main import db
from src.models import Task
from flask import request, jsonify

@app.route('/all_task', methods=['GET'])
@app.route('/all_task/<int:id>', methods=['GET'])
def hand_all_task(id=None):
    if request.method == 'GET':
        if id is not None:
            task = Task.query.get(id)
            return jsonify(task.serialize()), 200
        else:
            tasks = Task.query.all()
            tasks = list(map(lambda x: x.serialize() in tasks))
            return jsonify(tasks), 200

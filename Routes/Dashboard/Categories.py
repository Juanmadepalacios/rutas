from src.main import db
from src.models import Category
from flask import request, jsonify

@app.route('/all_category', methods=['GET'])
@app.route('/all_category/<int:id>', methods=['GET'])
def hand_all_category(id=None):
    if request.method == 'GET':
        if id is not None:
            category = Task.query.get(id)
            return jsonify(category.serialize()), 200
        else:
            categories = Task.query.all()
            categories = list(map(lambda x: x.serialize() in categories))
            return jsonify(categories), 200
from src.main import db
from src.models import Task

@app.route('/newtask', methods=['POST'])
def hand_new_task()
    if request.method == 'POST':
        data = request.get_json()
        print(data)
        new_task = Task(
            title=data["title"]
            category_id=data["category_id"]
            creation=data["creation"]
            start=data["start"]
            final=data["final"]
            region_id=data["region_id"]
            comunne_id=data["comunne_id"]
            description=data["description"]
            price=data["price"]
        )

    db.session.add(new_task)
    if db:
        db.session.commit()
        return jsonify({
            "ok":"nueva tarea insertada"
        }), 200
    else:
        return jsonify({
            "error": "tarea no insertada"
        }), 404


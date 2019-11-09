from flask_mail import Mail, Message
from flask_cors import CORS
from src.main import app


db = SQLAlchemy(app)
db.init_app(app)

CORS(app)
mail = Mail(app)

def sendmail():
    msg = Message('Hello',
        sender = 'tareas4geeks@gmail.com',
        recipients = ['juanma36@gmail.com']
    )
    msg.subject = "Esto es una prueba"
    msg.html = "<h1>Hola Mundo</h1>"
    mail.send(msg)

    return jsonify({"message":"Email sent"}), 200


@app.route('/test-mail', methods=['GET'])
def home():
    resp = sendmail()

    return jsonify(resp), 200
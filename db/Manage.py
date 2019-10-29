from flask import Flask
from flask_mail import Mail


app = Flask(__name__)
mail = Mail(app)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key'
app.config['DEBUG'] = True
app.config['ENV'] = 'development'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(BASEDIR, 'test.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'tareas4geeks@gmail.com
app.config['MAIL_PASSWORD'] = '4geeks2019'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['JWT_EXPIRATION_DELTA'] = datetime.timedelta(days=3)
db.init_app(app)
CORS(app)

'''
MAIL_SERVER : default ‘localhost’
MAIL_PORT : default 25
MAIL_USE_TLS : default False
MAIL_USE_SSL : default False
MAIL_DEBUG : default app.debug
MAIL_USERNAME : default None
MAIL_PASSWORD : default None
MAIL_DEFAULT_SENDER : default None
MAIL_MAX_EMAILS : default None
MAIL_SUPPRESS_SEND : default app.testing
MAIL_ASCII_ATTACHMENTS : default False
'''


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


if __name__ == '__main__':
    Manager.run()
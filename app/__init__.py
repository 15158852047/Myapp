from flask import Flask
from flask_mongoengine import MongoEngine


app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
app.config['MONGODB_SETTINGS'] = {
    'db': 'Myapp',
    'host': '127.0.0.1',
    'port': 27017
}


db = MongoEngine()
db.init_app(app)


from app.admin import admin
from app.user import user
app.register_blueprint(admin,url_prefix='/admin')
app.register_blueprint(user)
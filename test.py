from app import app
from app.models import User
from flask_script import Manager

manage = Manager(app)

@manage.command
def save():
    todo = User(username='study flask')
    todo.save()



if __name__ =='__main__':
    manage.run()
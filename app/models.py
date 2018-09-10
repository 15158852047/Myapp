from app import db
from datetime import datetime

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    username = db.Column(db.String(30),nullable=False,unique=True)
    password = db.Column(db.String(30),nullable=False)
    name = db.Column(db.String(60))
    tel = db.Column(db.String(15),unique=True)
    birth = db.Column(db.String(10))
    money = db.Column(db.Integer)
    jifen = db.Column(db.Integer)
    Role = db.Column(db.Integer,default=1)#0代表管理员，1会员
    money1 = db.relationship('Money', backref=db.backref('users'))
    message = db.relationship('Message', backref=db.backref('users'))


class Message(db.Model):
    __tablename__ = 'messages'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    addtime = db.Column(db.DateTime,default=datetime.now())
    title = db.Column(db.String(200))
    info = db.Column(db.Text)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))

class Money(db.Model):
    __tablename__ = 'money'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    money = db.Column(db.Integer)
    jifen = db.Column(db.Integer)
    payfor = db.Column(db.String(100))
    addtime = db.Column(db.DateTime,default=datetime.now())
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))



class Product(db.Model):
    __tablename__ = 'produces'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30),nullable=False)
    money = db.Column(db.Integer)
    Info = db.Column(db.String(200))
    have = db.Column(db.Integer)

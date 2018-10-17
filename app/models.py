from datetime import datetime
from app import db

class User(db.Document):
    username = db.StringField()
    password = db.StringField()
    name = db.StringField()
    tel = db.StringField()
    birth = db.StringField()
    money = db.IntField()
    jifen = db.IntField()
    Role = db.IntField()

class Message(db.Document):
    addTime = db.DateTimeField(default=datetime.now())
    info = db.StringField()
    isRead = db.IntField(default=0)

class Money(db.Document):
    money = db.IntField()
    jifen = db.IntField()
    payfor = db.StringField()
    addtime = db.DateTimeField(default=datetime.now())


class Product(db.Document):
    name = db.StringField()
    money = db.IntField()
    Info = db.StringField()
    have = db.IntField()#库存
    image = db.FileField()
    zhonglei = db.StringField()


class BuyCar(db.Document):#购物车
    ProdName = db.StringField()#物品名字
    Price = db.IntField()#价格
    Num = db.IntField()#数量
    AllPrice = db.IntField()#总价
    addTime = db.DateTimeField(default=datetime.now())#添加时间
    image = db.FileField()#物品的图片
    bname = db.StringField()


class Order(db.Document):#订单
    ProdName = db.StringField()
    Price = db.IntField()
    Num = db.IntField()
    AllPrice = db.IntField()
    addTime = db.DateTimeField(default=datetime.now())
    image = db.FileField()
    isRead = db.IntField()#0表示未读订单   1表示已读
    oname = db.StringField()

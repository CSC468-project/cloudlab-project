from time import time
import flask_sqlalchemy
import datetime

db = flask_sqlalchemy.SQLAlchemy()

db.config['SQLALCHEMY_DATABASE_URI'] = 'GET URI OF DATABASE?'
db.config['SQLALCHEMY_TRACK_MODIFCATIONS'] = False



class Orders(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.datetime )
    address = db.Column(db.String(100))
    phone_number = db.Column(db.Integer)
    sub_total = db.Column(db.Integer)
    tip = db.Colun(db.Integer)
    total = db.Column(db.Integer)
    food = db.Column(db.String(100))

class Menu(db.Model):
    __tablename__ = 'menu'
    food_type = db.Column(db.String(100))
    cost = db.Column(db.Integer)
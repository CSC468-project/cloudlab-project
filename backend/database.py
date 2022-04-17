from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

database = Flask(__name__)
database.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
database.config['SQLALCHEMY_TRACK_MODIFCATIONS'] = False
db = SQLAlchemy(database)


class Customer(db.Model):
    __tablename__ = 'customer'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable = False)
    last_name = db.Column(db.String(50), nullable = False)
    address = db.Column(db.String(500), nullable = False)
    city = db.Column(db.String(50), nullable = False)
    postcode = db.Column(db.String(50), nullable = False)
    email = db.Column(db.String(50), nullable = False, unique = True)
    phone_number = db.Column(db.String(50), nullable = False, unique = True)

    orders = db.relationship('Order', backref = 'customer')

order_menu = db.Table('order_menu',
    db.Column('order_id', db.Integer, db.ForeignKey('order.id'), primary_key = True),
    db.Column('menu_id', db.Integer, db.ForeignKey('menu.id'), primary_key = True)
)

class Order(db.Model):
    __tablename__ = 'order'
    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
    sub_total = db.Column(db.Integer)
    tip = db.Column(db.Integer)
    total = db.Column(db.Integer)
    
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable = False)
    menu = db.relationship('Menu', secondary = order_menu)

class Menu(db.Model):
    __tablename__ = 'menu'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable = False, unique = True)
    price = db.Column(db.Integer, nullable = False)
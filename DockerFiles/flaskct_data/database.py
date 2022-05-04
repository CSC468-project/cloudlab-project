import os
import random

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine(
    'mysql://root:mysql_root_123@' + os.getenv("CLOUDCOOKED_SERVICE_MYSQL_SERVICE_HOST") + ':3306/db')

db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

from models import Customer, Menu, Order


def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    Base.metadata.create_all(bind=engine)
    items = [Menu(name="Pizza", price="3.50",
                  url="https://images.unsplash.com/photo-1513104890138-7c749659a591?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1740&q=80"),
             Menu(name="Fries", price="2.50",
                  url="https://images.unsplash.com/photo-1518013431117-eb1465fa5752?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1740&q=80"),
             Menu(name="Soda", price="1.75",
                  url="https://images.unsplash.com/photo-1581636625402-29b2a704ef13?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=776&q=80")]
    for item in items:
        db_session.add(item)
    db_session.commit()


def get_menu_items():
    return Menu.query.all()


def get_order_items():
    return Customer.query.all()


def add_order(order):
    Base.metadata.create_all(bind=engine)
    to_add = Customer(random.randint(0, 100000000), order.get("name"), order.get("email"),
                      order.get("phone"),
                      order.get("street"), order.get("city"), order.get("state"),
                      order.get("zip"))
    db_session.add(to_add)
    db_session.commit()


def get_menu_index():
    from models import Menu
    s = set()
    for item in Menu.query.all():
        s.add(item.title)
    return s


""" Please dont remove this yet lol
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
"""

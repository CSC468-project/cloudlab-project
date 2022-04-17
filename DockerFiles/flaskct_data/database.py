from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('mysql://root:mysql_root_123@127.0.0.1:3306/db')
Base_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = Base_session.query_property()

def init_Base():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_Base()
    # import yourapplication.models
    Base.metadata.create_all(bind=engine)





class Customer(Base.Model):
    __tablename__ = 'customer'
    id = Base.Column(Base.Integer, primary_key=True)
    first_name = Base.Column(Base.String(50), nullable = False)
    last_name = Base.Column(Base.String(50), nullable = False)
    address = Base.Column(Base.String(500), nullable = False)
    city = Base.Column(Base.String(50), nullable = False)
    postcode = Base.Column(Base.String(50), nullable = False)
    email = Base.Column(Base.String(50), nullable = False, unique = True)
    phone_number = Base.Column(Base.String(50), nullable = False, unique = True)

    orders = Base.relationship('Order', backref = 'customer')

order_menu = Base.Table('order_menu',
    Base.Column('order_id', Base.Integer, Base.ForeignKey('order.id'), primary_key = True),
    Base.Column('menu_id', Base.Integer, Base.ForeignKey('menu.id'), primary_key = True)
)

class Order(Base.Model):
    __tablename__ = 'order'
    id = Base.Column(Base.Integer, primary_key=True)
    time = Base.Column(Base.DateTime, nullable = False, default = datetime.utcnow)
    sub_total = Base.Column(Base.Integer)
    tip = Base.Column(Base.Integer)
    total = Base.Column(Base.Integer)
    
    customer_id = Base.Column(Base.Integer, Base.ForeignKey('customer.id'), nullable = False)
    menu = Base.relationship('Menu', secondary = order_menu)

class Menu(Base.Model):
    __tablename__ = 'menu'
    id = Base.Column(Base.Integer, primary_key=True)
    name = Base.Column(Base.String(100), nullable = False, unique = True)
    price = Base.Column(Base.Integer, nullable = False)
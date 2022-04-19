from re import A, T
from unicodedata import name
from sqlalchemy import Column, Integer, String, ForeignKey, Table, DateTime
from datetime import datetime
from database import Base
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from sqlalchemy.types import DateTime, Float

class Customer(Base):
    __tablename__ = 'customer'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable = False)
    last_name = Column(String(50), nullable = False)
    address = Column(String(500), nullable = False)
    city = Column(String(50), nullable = False)
    postcode = Column(String(50), nullable = False)
    email = Column(String(50), nullable = False, unique = True)
    phone_number = Column(String(50), nullable = False, unique = True)

    orders = relationship('Order', backref = 'customer')


    def __init__(self, first_name, last_name, address, city, postcode, email, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.city = city
        self.postcode = postcode
        self.email = email
        self.phone_number = phone_number

    def __repr__(self):
        return f'<User {self.name!r}>'

order_menu = Table('order_menu', Base.metadata,
    Column('order_id', Integer, ForeignKey('order.id'), primary_key = True),
    Column('menu_id', Integer, ForeignKey('menu.id'), primary_key = True)
)

class Order(Base):
    __tablename__ = 'order'
    id = Column(Integer, primary_key=True)
    time = Column(DateTime, nullable = False, default = datetime.utcnow())
    sub_total = Column(Integer)
    tip = Column(Integer)
    total = Column(Integer)
    
    customer_id = Column(Integer, ForeignKey('customer.id'), nullable = False)
    menu = relationship('Menu', secondary = order_menu)


    def __init__(self, sub_total, tip, total):
        self.sub_total = sub_total
        self.tip = tip
        self.total = total

    def __repr__(self):
        return f'<User {self.name!r}>'


class Menu(Base):
    __tablename__ = 'menu'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable = False, unique = True)
    price = Column(Float(precision=4), nullable = False)
    url = Column(String(5000), nullable = False, unique = True)

    def __init__(self, name, price, url):
        self.name = name
        self.price = price
        self.url = url

    def __repr__(self):
        return f'<User {self.name!r}>'
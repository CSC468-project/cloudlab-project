from re import A, T
from unicodedata import name
from sqlalchemy import Column, Integer, String, ForeignKey, Table, DateTime
from datetime import datetime
from database import Base
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from sqlalchemy.types import DateTime, Float

order_menu = Table('order_menu', Base.metadata,
                   Column('order_id', Integer, ForeignKey('order.id'), primary_key=True),
                   Column('menu_id', Integer, ForeignKey('menu.id'), primary_key=True)
                   )


class Customer(Base):
    __tablename__ = 'customer'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    address = Column(String(500), nullable=False)
    city = Column(String(50), nullable=False)
    zip = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False, unique=True)
    phone_number = Column(String(50), nullable=False, unique=True)
    order = Column(String(10000), nullable=False)

    orders = relationship('Order', backref='customer')

    def __init__(self, id, name, email, phone_number, street, city, state, zip, order):
        self.id = id
        self.name = name
        self.email = email
        self.phone_number = phone_number
        self.street = street
        self.city = city
        self.state = state
        self.zip = zip
        self.order = order

    def __repr__(self):
        return f'<User {self.name!r}>'


class Order(Base):
    __tablename__ = 'order'
    id = Column(Integer, primary_key=True)
    time = Column(DateTime, nullable=False, default=datetime.utcnow())
    sub_total = Column(Integer)
    tip = Column(Integer)
    total = Column(Integer)

    customer_id = Column(Integer, ForeignKey('customer.id'), nullable=False)
    menu = relationship('Menu', secondary=order_menu)

    def __init__(self, sub_total, tip, total):
        self.sub_total = sub_total
        self.tip = tip
        self.total = total

    def __repr__(self):
        return f'<User {self.name!r}>'


class Menu(Base):
    __tablename__ = 'menu'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, unique=True)
    price = Column(Float(precision=4), nullable=False)
    url = Column(String(1000), nullable=False)

    def __init__(self, name, price, url):
        self.name = name
        self.price = price
        self.url = url

    def __repr__(self):
        return f'<User {self.name!r}>'

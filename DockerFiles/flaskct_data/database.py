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


def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    from models import Menu
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
    from models import Menu
    return Menu.query.all()


def add_order(order):
    from models import Customer
    Customer.metadata.create_all(bind=engine)
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

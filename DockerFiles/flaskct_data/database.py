from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('mysql://root:mysql_root_123@127.0.0.1:3306/db')

db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    import models
    Base.metadata.create_all(bind=engine)
    items = [Menu("Pizza", "3.50"), Menu("Fries", "$2.50"), Menu("Soda", "$1.75")]
    for item in items:
        db_session.add(item)
    db_session.commit()


def get_menu_items():
    import models
    return Menu.query.all()


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
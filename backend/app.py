from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from markupsafe import escape
import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost/flask'
app.config['SQLALCHEMY_TRACK_MODIFCATIONS'] = False

db = SQLAlchemy(app)



@app.route("/", methods = ['GET'])
def get_articles():
    return jsonify({"Hello":"World"})

@app.route("/new", methods = ['GET'])
def new_order():
    # order_id, time, address, phone number, cost, tip, food
    pass

def get_order():

    pass



if __name__ == "__main__":
    app.run(debug=True)
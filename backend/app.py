from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost/flask'
app.config['SQLALCHEMY_TRACK_MODIFCATIONS'] = False

db = SQLAlchemy(app)


class Articles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    body = db.Column(db.Text())
    date = db.Column(db.DateTime, default = datetime.datetime.now)


    def __init__(self, title, body):
        self.title = title
        self.body = body

class ArticleSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'body', 'date')


article_schema = ArticleSchema()

@app.route("/", methods = ['GET'])
def get_articles():
    return jsonify({"Hello":"World"})

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, request, render_template, jsonify

app = Flask(__name__)


def do_something(text1, text2):
    text1 = text1.upper()
    text2 = text2.upper()
    combine = text1 + "+" + text2
    return combine


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/join', methods=['GET', 'POST'])
def my_form_post():
    text1 = request.form['text1']
    word = request.args.get('text1')
    text2 = request.form['text2']
    combine = do_something(text1, text2)
    result = {
        "output": combine
    }
    result = {str(key): value for key, value in result.items()}
    return jsonify(result=result)


""" 
/! Where `items` is our list of menu items from the database.                   !/
/! Renders a menu pages from the 'flaskct_data/templates/menu.html' template.   !/

@app.route('/menu', methods=['GET'])
def menu_route():
     return render_template('menu.html', len = len(items), items = items)
"""


if __name__ == '__main__':
    app.run(host="0.0.0.0")

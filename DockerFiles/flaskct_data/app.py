from flask import Flask, request, render_template, jsonify, send_from_directory
from database import get_menu_items, get_menu_index

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


@app.route('/menu', methods=['GET', 'POST'])
def menu_search():
    items = get_menu_items()
    return render_template('menu.html', len=len(items), items=items)


@app.route('/order_submitted', methods=['GET', 'POST'])
def order_submitted():
    print(request.form)
    return render_template('order_submitted.html')


@app.route('/static/<path:path>', methods=['GET'])
def static_resources(path):
    return send_from_directory('static', path)


if __name__ == '__main__':
    app.run(host="0.0.0.0")

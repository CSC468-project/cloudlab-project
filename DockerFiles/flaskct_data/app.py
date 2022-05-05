from flask import Flask, request, render_template, jsonify, send_from_directory
from database import get_menu_items, add_order, get_order_items, get_orders_by_id, remove_orders_by_id
import sys

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
    if request.method == 'POST':
        print(request.form, file=sys.stderr)
        add_order(request.form)
    return render_template('order_submitted.html')


@app.route('/orders', methods=['GET', 'POST'])
def orders():
    if request.method == 'POST':
        print(request.form, file=sys.stderr)
        orders = []
        for key in request.form:
            if "orderid" in key:
                if request.form.get(key) == "on":
                    orders.append(key.split("_")[1])

        orders_for_route = get_orders_by_id(orders)

        route_list = []
        for order in orders_for_route:
            route_list.append("{} {} {}".format(order.address, order.city, order.zip))

        remove_orders_by_id(orders)
        return URL_builder(route_list)

    orders = get_order_items()
    formatted_orders = []
    for customer in orders:
        to_add = ""
        food = customer.order.split("_")
        for x in range(0, len(get_menu_items())):
            to_add = to_add + get_menu_items()[x].name + " Quantity: " + food[x] + "\n"
        formatted_orders.append(to_add)
    return render_template('orders.html', len=len(orders), items=orders, orders=formatted_orders)


@app.route('/static/<path:path>', methods=['GET'])
def static_resources(path):
    return send_from_directory('static', path)


import urllib.parse


def URL_builder(addresses):
    # Takes in an addresses as a ordered list of strings and returns a link to google maps for the route
    stops = len(addresses)
    destination = urllib.parse.quote(addresses[-1])
    waypoints = ""
    url = "https://www.google.com/maps/dir/?api=1&destination={}".format(destination)
    if stops > 1:
        # Creates a string with addresses separated by the '|' character
        for stop in addresses[:-1]:
            waypoints += stop + '|'
        # Adds the parased string to URL excluding the trailing '|'
        url += "&waypoints=" + urllib.parse.quote(waypoints[:-1])
    # ensures google maps will always know to make it driving instructions
    url += "&travelmode=driving"

    return url


if __name__ == '__main__':
    app.run(host="0.0.0.0")

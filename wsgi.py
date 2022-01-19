# wsgi.py
# pylint: disable=missing-docstring

from os import abort
from flask import Flask, render_template, jsonify, abort, request
app = Flask(__name__)

PRODUCTS = {
    1: { 'id': 1, 'name': 'Skello' },
    2: { 'id': 2, 'name': 'Socialive.tv' },
    3: { 'id': 3, 'name': 'Crunchyroll.tv' },
}

API_URL = '/api/v1/'

@app.route('/')
def hello():
    return "Hello World!"

# Get all products
@app.route(f"{API_URL}products", methods=['GET'])
def products_action():
    res = []

    for p in PRODUCTS.items():
        res.append(p[1])
    
    return jsonify(res)

# Save product
@app.route(f"{API_URL}products", methods=['POST'])
def save_product_action():
    req = request.get_json()

    data = {
        'id': len(PRODUCTS) + 1,
        'name': req['name']
    }

    return jsonify(data)

# Get product by id
@app.route(f"{API_URL}products/<int:id>", methods=['GET'])
def get_product_action(id):
    r = PRODUCTS.get(id)

    if r is not None:
        return jsonify(r)

    else:
        abort(404)

# Delete product
@app.route(f"{API_URL}products/<int:id>", methods=['DELETE'])
def delete_product_action(id):
    if PRODUCTS.get(id) is not None:
        return '', 204
    else:
        abort(404)

# Update product
@app.route(f"{API_URL}products", methods=['PUT'])
def update_product_action():
    req = request.get_json()

    if 'id' not in req:
        return jsonify({'error':"Clé 'id' absent"}), 422

    if 'name' not in req:
        return jsonify({'error':"Clé 'name' absent"}), 422

    product_id = req['id']
    name = req['name']

    if PRODUCTS.get(product_id) is None:
        return render_template('page_not_found.html'), 404

    return '', 204

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404
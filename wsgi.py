# wsgi.py
# pylint: disable=missing-docstring

from os import abort
from flask import Flask, render_template, jsonify, abort
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

@app.route(f"{API_URL}products")
def products_action():
    res = []

    for p in PRODUCTS.items():
        res.append(p[1])
    
    return jsonify(res)

@app.route(API_URL + 'products/<int:id>')
def get_product_action(id):
    r = PRODUCTS.get(id)

    if r is not None:
        return jsonify(r)

    else:
        abort(404)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404
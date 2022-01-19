# wsgi.py
# pylint: disable=missing-docstring

from flask import Flask
from flask import jsonify
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
    
    return jsonify(PRODUCTS)
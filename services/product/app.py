from flask import Flask, jsonify
import requests

app = Flask(__name__)

PRODUCTS = {
    '1' : {'name' : 'Augustiner'},
    '2' : {'name' : 'Paulaner '},
    '3' : {'name' : 'Franziskaner'}
}

def price(id):
    r = requests.get('http://price/{}'.format(id))
    return r.json()['price']

@app.route('/')
def products():
    return jsonify(PRODUCTS)

@app.route('/<id>')
def product(id):
    p = PRODUCTS[id].copy()
    p['price'] = price(id)
    return jsonify(p)

@app.route('/health')
def health():
    return jsonify({'status':'OK'})

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')

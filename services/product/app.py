from flask import Flask, jsonify

app = Flask(__name__)

PRODUCTS = {
    '1' : {'name' : 'Augustiner'},
    '2' : {'name' : 'Paulaner '},
    '3' : {'name' : 'Franziskaner'}
}


@app.route('/')
def products():
    return jsonify(PRODUCTS)

@app.route('/<code>')
def product(code):
    return jsonify(PRODUCTS[code])

@app.route('/health')
def health():
    return jsonify({'status':'OK'})

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')

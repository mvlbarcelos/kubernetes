from flask import Flask, jsonify

app = Flask(__name__)

PRICE = {
    '1' : {'price' : 0.79},
    '2' : {'price' : 1.00},
    '3' : {'price' : 0.69},
}

@app.route('/<id>')
def price(id):
    return jsonify(PRICE[id])

@app.route('/health')
def health():
    return jsonify({'status':'OK'})

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')

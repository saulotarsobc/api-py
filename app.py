from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/hello', methods=['GET'])
def hello():
    return jsonify(message="Hello, World!")


@app.route('/a', methods=['GET'])
def hello_a():
    return jsonify(message="a")


@app.route('/b', methods=['GET'])
def hello_b():
    return jsonify(message="b")


@app.route('/c', methods=['GET'])
def hello_c():
    return jsonify(message="c")


@app.route('/d', methods=['GET'])
def hello_d():
    return jsonify(message="d")


@app.route('/e', methods=['GET'])
def hello_e():
    return jsonify(message="e")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

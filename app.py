from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/', methods=['GET'])
def route_1():
    people = [
        {"id": 1, "name": "Alice", "age": 30, "email": "alice@example.com"},
        {"id": 2, "name": "Bob", "age": 25, "email": "bob@example.com"},
        {"id": 3, "name": "Charlie", "age": 35, "email": "charlie@example.com"},
        {"id": 4, "name": "David", "age": 40, "email": "david@example.com"},
        {"id": 5, "name": "Eve", "age": 28, "email": "eve@example.com"}
    ]
    courses = [
        {"id": 1, "name": "Introduction to Programming",
            "description": "Learn the basics of programming"},
        {"id": 2, "name": "Advanced Python Programming",
            "description": "Master the art of Python programming"},
        {"id": 3, "name": "Data Science with Python",
            "description": "Get started with data science with Python"},
        {"id": 4, "name": "Machine Learning with Python",
            "description": "Master machine learning with Python"},
        {"id": 5, "name": "Deep Learning with Python",
            "description": "Explore deep learning with Python"}
    ]

    return jsonify({"people": people, "courses": courses})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World!"

@app.route('/api/add', methods=['POST'])
def add():
    data = request.get_json()
    a = data.get('a', 0)
    b = data.get('b', 0)
    result = a + b
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True, port=5000)

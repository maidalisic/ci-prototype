from flask import Flask, request, jsonify
from flask_cors import CORS
from simpleeval import SimpleEval

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})  # Erlaubt CORS für alle Domains auf allen /api/ Routen

@app.route('/')
def home():
    return "Hello, World!"

@app.route('/api/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    expression = data.get('expression', "")
    try:
        evaluator = SimpleEval()
        result = evaluator.eval(expression)
        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True, port=5000)

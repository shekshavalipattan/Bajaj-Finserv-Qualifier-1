from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/bfhl', methods=['POST'])
def handle_post():
    data = request.get_json()
    response = process_data(data)
    return jsonify(response)

@app.route('/bfhl', methods=['GET'])
def handle_get():
    return jsonify({"operation_code": 1})

def process_data(data):
    numbers = []
    alphabets = []
    highest_lowercase_alphabet = None

    for item in data['data']:
        if item.isdigit():
            numbers.append(item)
        elif item.isalpha():
            alphabets.append(item)
            if item.islower():
                if highest_lowercase_alphabet is None or item > highest_lowercase_alphabet:
                    highest_lowercase_alphabet = item

    response = {
        "is_success": True,
        "user_id": "john_doe_17091999",
        "email": "john@xyz.com",
        "roll_number": "ABCD123",
        "numbers": numbers,
        "alphabets": alphabets,
        "highest_lowercase_alphabet": [highest_lowercase_alphabet] if highest_lowercase_alphabet else []
    }

    return response

if __name__ == '__main__':
    app.run(debug=True)

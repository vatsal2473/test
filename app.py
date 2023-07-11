from flask import Flask, render_template, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/alert_message', methods=['POST'])
def alert_message():
    data = request.json
    print(data)

    message = data['message']


    # You can perform any necessary processing here based on the data received

    response = {
        'result': 'success',
        'message': f"hello {message}"
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run()

from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

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
        'message': f'Alert message: {message}'
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run()

from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    if (request.method == 'POST'):
        some_json = request.get_json()
        return jsonify({'req_msg' : some_json}), 201
    else:
        return jsonify({"message": "Hello World"})

@app.route('/multi/<int:num>', methods=['GET'])
def multiply(num):
    return jsonify({'result': num**2})

if __name__ == '__main__':
    app.run(debug=True)
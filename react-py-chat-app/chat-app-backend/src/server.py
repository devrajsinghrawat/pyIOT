from flask import Flask, request
from flask_restful import Resource, Api, abort

app = Flask(__name__)
api = Api(app)

users = []

class User(Resource):
    def get(self):
        return {'about': 'Hello World'}

    def post(self):
        # username = request.json['username']∏
        username = request.get_json()
        user_taken = username in users
        if user_taken:
            abort(403)
        else:
            users.append(username)
            return 'Success in Login'

api.add_resource(User, '/login')

if __name__ == '__main__':
    app.run(debug=True)
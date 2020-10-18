from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from item import Item, ItemList
from user import UserRegister
from security import authenticate, identity

app = Flask(__name__)
api = Api(app)
app.secret_key = 'sarthak'

jwt = JWT(app, authenticate, identity)

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    app.run(port=5000)

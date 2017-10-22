from flask import Flask

from flask_restful import Api
from auth import authenticate, identity
from client import ModifyClient, GetClient, ClientList
from flask_jwt import JWT

restApp = Flask(__name__)
restApp.secret_key = "flaskRest"
api = Api(restApp)

jwt = JWT(restApp, authenticate, identity)  # /auth


# adding the resources to the api
api.add_resource(ModifyClient, '/client')
api.add_resource(GetClient, '/client/<int:id>')
api.add_resource(ClientList, '/clients')

if __name__ == '__main__':
    restApp.run(debug=True)
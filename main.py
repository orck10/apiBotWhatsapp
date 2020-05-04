from views.mensagemApp import *
from flask import Flask
from flask_restful import Api

app = Flask(__name__)
api = Api(app)

api.add_resource(HelloWorld, '/')
api.add_resource(ReceberMSG, '/api/mensagem')

if __name__ == '__main__':
    app.run(debug=True)
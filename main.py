from views.mensagemApp import *
from flask import Flask
from flask_restful import Api
#from  configparser import ConfigParser

'''
config = ConfigParser()
config["MONGO"] = { "host":"$host$",
                    "port":"$port$",
                    "username":"$username$",
                    "password":"$password$",
                    "authSource":"$authSource$",
                    "db":"$db$",
                    "collection":"$collection$"}
with open('./mongo.conf', 'w') as configfile:
    config.write(configfile)
'''

app = Flask(__name__)
api = Api(app)

api.add_resource(HelloWorld, '/')
api.add_resource(ReceberMSG, '/api/mensagem')

if __name__ == '__main__':
    app.run(debug=True)
from models.dtoMensagem import DTOMensagem
from conectionMongo.templateRest import templateJson
import json
from flask_restful import reqparse, abort, Resource

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

class ReceberMSG(Resource): 
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('mensagem', required=True)
        parser.add_argument('nomes', location='json', type=list)
        parser.add_argument('numeroTelefone', location='json', type=list)
        args = parser.parse_args()
        dto = DTOMensagem()
        dto.mensagem = args['mensagem']
        dto.nomes =  args['nomes']
        dto.numeroTelefone = args['numeroTelefone']
        dto.id = dto.insert()
        dados_json = templateJson(dto.id,"200")
        return dados_json, 201 
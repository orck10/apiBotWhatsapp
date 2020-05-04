from conectionMongo.conectionMongo import Mongo
from conectionMongo.templateRest import parseJson
import json

class DTOMensagem:
    def __init__(self):
        self.id = ""
        self.mensagem = ""
        self.nomes=[]
        self.numeroTelefone = []
        self.enviado = False
    
    def insert(self):
        dic = {}
        dic['mensagem'] = self.mensagem
        dic['nomes'] = []
        dic['numeros'] = []
        if self.nomes:
            for n in self.nomes:
                dic['nomes'].append(n)
        if self.numeroTelefone:
            for n in self.numeroTelefone:
                dic['numeros'].append(n)
        if(self.enviado):
            dic['enviado'] = 1
        else:
            dic['enviado'] = 0
        mongoConection = Mongo()
        self.id = mongoConection.insert(dic)
        return self.id
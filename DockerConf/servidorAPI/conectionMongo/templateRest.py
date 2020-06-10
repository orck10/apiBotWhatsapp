import json

def templateJson(dados, status):
    dic = {}
    dic['resp'] = dados
    dic['status'] = status
    return json.dumps(dic)

def parseJson(obj):
    dic = {}
    dic['dados'] = obj
    return json.dumps(dic)
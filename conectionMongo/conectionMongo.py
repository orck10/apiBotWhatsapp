from pymongo import MongoClient
from  configparser import ConfigParser

config = ConfigParser()
config.read("./mongo.conf")

class Mongo:
    def __init__(self):
        self.client = MongoClient(host=config.get("MONGO","host"),
                    port=int(config.get("MONGO","port")), 
                    username=config.get("MONGO","username"), 
                    password=config.get("MONGO","password"),
                    authSource=config.get("MONGO","authSource"))
        self.db = self.client[config.get("MONGO","db")]
        self.collection = self.db[config.get("MONGO","collection")]
    
    def insert(self, data):
        obj_id = self.collection.insert_one(data).inserted_id
        return str(obj_id)

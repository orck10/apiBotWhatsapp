from pymongo import MongoClient

class Mongo:
    def __init__(self):
        self.client = MongoClient(host="192.168.99.100",
                    port=27017, 
                    username="root", 
                    password="123456",
                    authSource="admin")
        self.db = self.client['dadoswhats']
        self.collection = self.db['dadoswhats']
    
    def insert(self, data):
        obj_id = self.collection.insert_one(data).inserted_id
        return str(obj_id)

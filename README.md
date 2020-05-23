# BOT API

This is a api receive a message to save at MongoDB, where the bot will consult to send at Whatsapp


## REQUIRIMENTS

### Is madatory to run this project with mongoDB
#### At the near future I will add a new version with a mongo in docker configuration
At 'connection Mongo/connection.py', insert the mongodb parameters Like:

```
self.client = MongoClient(host=$host$,
                    port=$port$, 
                    username=$username$, 
                    password=$password$,
                    authSource=$authSource$)
        self.db = self.client['$dbName$']
        self.collection = self.db['$collectionName$']
```

### To run the project is necessary use python 3.6.+ and the pip installed

You did run :

```
    pip install requirements.txt
```

With this, all libs will be instaled

## Run the project

After install requirements run main.py 

```
    python  main.py
```

## Use API

The default addres is "127.0.0.1" and default port is "5000", the url is "127.0.0.1:5000"
The api path is "/api/mensagem"
To send mesages use the method "POST" 
The json body is like :

```
    {
	    "mensagem":"$Mesage text$",
	    "nomes":["$Contact Name$","$Contact Name$"]
    }
```


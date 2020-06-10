# BOT API

This is a api receive a message to save at MongoDB, where the bot will consult to send at Whatsapp


## REQUIRIMENTS
#### This project run with docker compose
For configure the database variables is mandatory create a file '.env' at /DockerConf, the file must contains:

```
    USERNAME=root
    PASSWORD=123456
    AUTHSOURCE=admin
    DB=whats
    COLLECTION=whats
```
## Run the project
### To run the project is necessary use docker and docker compose:

#### You could run at Docker Conf directory the follow commands:

For linux:

```
    sudo docker-compose -f startproject.yml up -d
```

For Windows :

```
    docker-compose -f startproject.yml up -d
```

## Use API

The default addres for linux is "127.0.0.1" and default port is "5000", the url is "127.0.0.1:5000", if it runs at windows, you must confirm your docker machine address
The api path is "/api/mensagem"
To send mesages use the method "POST" 
The json body is like :

```
    {
	    "mensagem":"$Mesage text$",
	    "nomes":["$Contact Name$","$Contact Name$"]
    }
```


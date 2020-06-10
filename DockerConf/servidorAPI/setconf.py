import sys
from  configparser import ConfigParser

dic = {}

for a in sys.argv:
	print(a)
	if a[0:5] == "host:":
		try:
			dic['host'] = a[5:]
		except:
			dic['host'] = ""
	
	if a[0:5] == "port:":
		try:
			dic['port'] = a[5:]
		except:
			dic['port'] = ""
	
	if a[0:9] == "username:":
		try:
			dic['username'] = a[9:]
		except:
			dic['username'] = ""

	if a[0:9] == "password:":
		try:
			dic['password'] = a[9:]
		except:
			dic['password'] = ""

	if a[0:11] == "authsource:":
		try:
			dic['authSource'] = a[11:]
		except:
			dic['authSource'] = ""
	if a[0:3] == "db:":
		try:
			dic['db'] = a[3:]
		except:
			dic['db'] = ""

	if a[0:11] == "collection:":
		try:
			dic['collection'] = a[11:]
		except:
			dic['collection'] = ""	

config = ConfigParser()
config["MONGO"] = { "host":dic['host'],
                    "port":dic['port'],
                    "username":dic['username'],
                    "password":dic['password'],
                    "authSource":dic['authSource'],
                    "db":dic['db'],
                    "collection":dic['collection']}
with open('./mongo.conf', 'w') as configfile:
    config.write(configfile)
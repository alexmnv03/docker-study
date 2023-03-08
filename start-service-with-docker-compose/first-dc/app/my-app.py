import pymongo import MongoClient
import pprint import pprint

MONGO_URL = "mongodb://mongo-srv:27017"
client = MongoClient(MONGO_URL)
db = client.admin
dbs_list = db.command("listDatabases")
pprint(dbs_list)

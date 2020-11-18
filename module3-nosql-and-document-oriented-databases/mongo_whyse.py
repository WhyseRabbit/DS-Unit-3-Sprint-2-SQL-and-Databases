import csv
import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

MONGO_USER = os.getenv("MONGO_USER", default="NUH_UH!")
MONGO_PW = os.getenv("MONGO_PW", default="NUH_UH!")
MONGO_CLUSTER = os.getenv("MONGO_CLUSTER_NAME", default="NUH_UH!")

connection_uri = f"mongodb+srv://{MONGO_USER}:{MONGO_PW}@{MONGO_CLUSTER}.mongodb.net/NoSQL-Stuff?retryWrites=true&w=majority"

client = MongoClient(connection_uri)

db = client.titanic_database

collection = db.titanic_stuff

with open("titanic.csv", "r") as f:
    reader = csv.DictReader(f)
    a = list(reader)

test_query = collection.insert_many(a)


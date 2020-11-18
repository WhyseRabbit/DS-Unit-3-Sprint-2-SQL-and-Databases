from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_USER = os.getenv("MONGO_USER", default="NUH_UH!")
MONGO_PW = os.getenv("MONGO_PW", default="NUH_UH!")
MONGO_CLUSTER = os.getenv("MONGO_CLUSTER_NAME", default="NUH_UH!")

connection_uri = f"mongodb+srv://{MONGO_USER}:{MONGO_PW}@{MONGO_CLUSTER}.mongodb.net/NoSQL-Stuff?retryWrites=true&w=majority"

client = MongoClient(connection_uri)

db = client.titanic_database

collection = db.titanic_stuff

test_query = collection.insert_one({
    "Survived" : 0,
    "PCclass" : 3,
    "Full_Name" : "Mr. Patrick Dooley",
    "Gender" : "male",
    "Age" : 32,
    "Sib_Spouse_Count" : 0,
    "Parent_Child_Count" : 0,
    "Fare" : 7.75
    })


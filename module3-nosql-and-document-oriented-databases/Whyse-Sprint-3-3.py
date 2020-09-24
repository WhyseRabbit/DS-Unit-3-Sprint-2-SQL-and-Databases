import os
from pdb import set_trace as breakpoint
from urllib.parse import quote_plus
import pymongo
from dotenv import load_dotenv
# import pandas as pd
# import dnspython


load_dotenv()

MONGO_USER = os.getenv("MONGO_USER", default="NOPE")
MONGO_PW = os.getenv("MONGO_PW", default="ZILCH")
CLUSTER_NAME = os.getenv("CLUSTER_NAME", default="NUNYA")

conn_uri = quote_plus("mongodb+srv://{MONGO_USER}:{MONGO_PW}@{CLUSTER_NAME}?retryWrites=true&w=majority")
client = pymongo.MongoClient(conn_uri)
print("URI:", conn_uri)

breakpoint()

ana_data = client.sample_analytics
print(ana_data.list_collection_names())

tran_call = ana_data.transactions
print(tran_call.count_documents({})
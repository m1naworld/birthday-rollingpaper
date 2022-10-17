from dotenv import load_dotenv
import os
from pymongo import MongoClient
import certifi

load_dotenv()
DB = os.getenv('DB')
client = MongoClient(DB, tlsCAFile=certifi.where())

db = client.dbrollingPage

# db.test.insert_one({"user": "미나"})
print("success")


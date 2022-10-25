from dotenv import load_dotenv
import os
from pymongo import MongoClient
import certifi

load_dotenv()
DB = os.getenv('DB')
client = MongoClient(DB, tlsCAFile=certifi.where())

db = client.dbrollingPage

print("success")


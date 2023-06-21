import os
from dotenv import load_dotenv

from pymongo import MongoClient
from productWC import get_products_data

load_dotenv()
username = os.getenv('MONGODB_USERNAME')
password = os.getenv('MONGODB_PASSWORD')

uri = f"mongodb+srv://{username}:{password}@cluster0.qlswjel.mongodb.net/"
client = MongoClient(uri)

db = client.test
print(db)



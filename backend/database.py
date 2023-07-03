import os, json
from dotenv import load_dotenv
from pymongo import MongoClient, errors

load_dotenv()
username = os.getenv("MONGODB_USERNAME")
password = os.getenv("MONGODB_PASSWORD")

uri = f"mongodb+srv://{username}:{password}@cluster0.qlswjel.mongodb.net/"
client = MongoClient(uri)

try:
    client.admin.command("ismaster")
    print("MongoDB 서버 연결 확인")
except errors.ConnectionFailure:
    print("MongoDB 서버 연결 불가")

db = client["products_database"]
products_collection = db["products"]
price_by_date_collection = db["price_by_date"]
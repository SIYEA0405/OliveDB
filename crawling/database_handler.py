import os
from dotenv import load_dotenv

from pymongo import MongoClient, errors
from productWC import get_products_data

load_dotenv()
username = os.getenv('MONGODB_USERNAME')
password = os.getenv('MONGODB_PASSWORD')

uri = f"mongodb+srv://{username}:{password}@cluster0.qlswjel.mongodb.net/"
client = MongoClient(uri)

# ====test====
# try:
#     # The ismaster command is cheap and does not require auth.
#     client.admin.command('ismaster')
# except errors.ConnectionFailure:
#     print("Server not available")

# db = client["my_database"]
# collection = db["my_collection"]

# # Try inserting a document
# try:
#     collection.insert_one({"test": "document"})
# except errors.ServerSelectionTimeoutError as err:
#     print("Could not connect to server: %s", err)
    
# # Try retrieving a document
# try:
#     document = collection.find_one()
#     print(document)
# except errors.ServerSelectionTimeoutError as err:
#     print("Could not connect to server: %s", err)



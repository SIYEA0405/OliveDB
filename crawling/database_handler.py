import os, json
from dotenv import load_dotenv

from pymongo import MongoClient, errors
from productWC import crawlProducts

load_dotenv()
username = os.getenv("MONGODB_USERNAME")
password = os.getenv("MONGODB_PASSWORD")
categoryNo = os.path.join(os.path.dirname(os.path.realpath(__file__)), "..", "test.json")

with open(categoryNo, "r") as nums:
    category_num_list = json.load(nums)

uri = f"mongodb+srv://{username}:{password}@cluster0.qlswjel.mongodb.net/"
client = MongoClient(uri)

try:
    client.admin.command("ismaster")
    print("MongoDB 서버 연결 확인")
except errors.ConnectionFailure:
    print("MongoDB 서버 연결 불가")

db = client["products_database"]
product_collection = db["products"]
price_by_date_collection = db["price_by_date"]


def all_pages_crawl():
    for category_dict in category_num_list:
        for category, numbers in category_dict.items():
            for number in numbers:
                product_datas, prices_by_date = crawlProducts(number)
                try:
                    product_collection.insert_many(product_datas["products_data"])
                    price_by_date_collection.insert_many(
                        prices_by_date["prices_by_date"]
                    )
                    print("데이터저장이 끝났습니다")
                except errors.ServerSelectionTimeoutError as err:
                    print("Could not connect to server: %s", err)
    return


all_pages_crawl()

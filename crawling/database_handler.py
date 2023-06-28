import os, json
from dotenv import load_dotenv

from pymongo import MongoClient, errors
from productWC import crawlProducts

load_dotenv()
username = os.getenv("MONGODB_USERNAME")
password = os.getenv("MONGODB_PASSWORD")
categoryNo = os.path.join(
    os.path.dirname(os.path.realpath(__file__)), "..", "test.json"
)

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
products_collection = db["products"]
price_by_date_collection = db["price_by_date"]


class ProductManager:
    def __init__(self):
        self.db = db
        self.products_collection = products_collection
        self.price_by_date_collection = price_by_date_collection

    def add_category(self, product_id, category):
        product = self.products_collection.find_one({"_id": product_id})
        if category not in product["small_ctg"]:
            self.products_collection.update_one(
                {"_id": product_id, "small_ctg": {"$ne": category}},
                {"$push": {"small_ctg": category}},
            )

    def update_product_name(self, product_id, new_name):
        self.products_collection.update_one(
            {"_id": product_id}, {"$set": {"name": new_name}}
        )

    def update_current_price(self, product_id, new_price):
        self.products_collection.update_one(
            {"_id": product_id}, {"$set": {"price.current": new_price}}
        )

    def update_lowest_price(self, product_id, new_lowest_price):
        product = self.products_collection.find_one({"_id": product_id})
        if (
            product
            and "price" in product
            and int(product["price"]["lowest"]) > int(new_lowest_price)
        ):
            self.products_collection.update_one(
                {"_id": product_id}, {"$set": {"price.lowest": new_lowest_price}}
            )


# class Product_update:
#     # small 카테고리 추가, 상품명변경, 현재가격 업데이트, 최저가 비교 후 업데이트
#     def __init__(self):
#         self.products = item

#     def get_item(self, id):
#         item = self.collection.find_one({"_id": id})
#         if item:
#             return item
#         else:
#             return "No item found with provided id."

#     def add_category(self, id, ctg):
#         item = self.get_item(id)
#         if ctg not in item["small_ctg"]:
#             item.update_one({"_id": id}, {"$push": {"small_ctg": ctg}})
#         return

#     def update_name(self, id, name):
#         self.collection.update_one({"_id": id}, {"$set": {"name": name}})
#         return

#     def update_price_current(self, id, cp):
#         item = self.get_item(id)
#         return item.update_one({"_id": id}, {"$set": {"price": {"current": cp}}})

#     def is_price_lowest(self, id, lp):
#         item = self.get_item(id)
#         ex_lp = item["price.lowest"]
#         if int(ex_lp) > int(lp):
#             item.update_one({"_id": id}, {"$set": {"price": {"lowest": lp}}})
#         return


def all_pages_crawl():
    for category_dict in category_num_list:
        for category, numbers in category_dict.items():
            for number in numbers:
                product_datas, prices_by_date = crawlProducts(number)
                try:
                    products_collection.insert_many(product_datas["products_data"])
                    price_by_date_collection.insert_many(
                        prices_by_date["prices_by_date"]
                    )
                    print("데이터저장이 끝났습니다")
                except errors.ServerSelectionTimeoutError as err:
                    print("Could not connect to server: %s", err)
    return


all_pages_crawl()

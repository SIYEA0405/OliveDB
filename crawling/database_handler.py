import os, time
from dotenv import load_dotenv

from datetime import datetime
from pymongo import MongoClient, errors
from productWC import crawlProducts
from categoryNo import category_numbers

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
product_collection = db["products"]
price_by_date_collection = db["price_by_date"]

now = datetime.now()


def time_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        elapsed_time_minutes = elapsed_time / 60
        print(f"\033[94m{func.__name__} 실행 시간: {elapsed_time}초")
        print(f"\033[35m{func.__name__} 실행 시간: {elapsed_time_minutes}분\033[0m")
        return result

    return wrapper


from datetime import datetime


def update_or_insert_product(new_product_date):
    current_date = now.strftime("%Y-%m-%d")
    new_price = new_product_date["dates"][-1]["price"]
    product_id = new_product_date["_id"]
    price_in_db = price_by_date_collection.find_one({"_id": product_id})

    if not price_in_db:
        price_by_date_collection.insert_one(new_product_date)

    else:
        if price_in_db["dates"][-1]["date"] == current_date:
            price_by_date_collection.update_one(
                {"_id": product_id, "dates.date": current_date},
                {"$set": {"dates.$.price": new_price}},
            )
        else:
            price_by_date_collection.update_one(
                {"_id": product_id},
                {"$push": {"dates": {"date": current_date, "price": new_price}}},
                upsert=True,
            )


@time_decorator
def all_pages_crawl():
    for category_dict in category_numbers:
        for category, numbers in category_dict.items():
            for index, number in enumerate(numbers):
                crawlDatas = crawlProducts(number)
                products_collection, date_collection = (
                    crawlDatas["products_collection"],
                    crawlDatas["date_collection"],
                )
                for product_data in products_collection:
                    try:
                        product_collection.update_one(
                            {"_id": product_data["_id"]},
                            {
                                "$set": {
                                    "name": product_data["name"],
                                    "price.current": product_data["price"]["current"],
                                },
                                "$addToSet": {
                                    "small_ctg": {"$each": product_data["small_ctg"]}
                                },
                                "$min": {
                                    "price.lowest": product_data["price"]["current"]
                                },
                                "$setOnInsert": {
                                    "brand": product_data["brand"],
                                    "price.original": product_data["price"]["original"],
                                    "large_ctg": product_data["large_ctg"],
                                },
                            },
                            upsert=True,
                        )
                    except errors.ServerSelectionTimeoutError as err:
                        print("Could not connect to server: %s", err)

                print("상품의 데이터 저장 완료")

                for product_date in date_collection:
                    try:
                        update_or_insert_product(product_date)
                    except errors.ServerSelectionTimeoutError as err:
                        print("Could not connect to server: %s", err)

                print("날짜 및 가격 데이터 저장 완료")
                print(
                    f"\033[104m{category}의 {index+1}/{len(numbers)} 데이터 저장이 완료\033[0m"
                )
            print(f"\033[42m{category}의 모든 데이터 저장이 완료되었습니다.\033[0m")
    return


all_pages_crawl()

from fastapi import APIRouter
from typing import List
from database import products_collection, price_by_date_collection
from schemas import Product, Price_by_date

products_router = APIRouter()


@products_router.get("/products", response_model=List[Product])
async def read_products():
    products = []
    for product in products_collection.find():
        products.append(Product(**product))
    return products


@products_router.get("/price-by-dates", response_model=List[Price_by_date])
async def read_price_by_dates():
    price_by_dates = []
    for price_by_date in price_by_date_collection.find():
        price_by_dates.append(Price_by_date(**price_by_date))
    return price_by_dates


@products_router.get("/{product_txt}", response_model=List[Product])
async def get_product(product_txt: str):
    regex = ".*".join(product_txt.split())
    products = []
    for product in products_collection.find(
        {"name": {"$regex": regex, "$options": "i"}}
    ):
        product["_id"] = str(product["_id"])
        products.append(Product(**product))
    return products

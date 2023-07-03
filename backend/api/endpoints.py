from fastapi import APIRouter
from typing import List
from backend.database import products_collection, price_by_date_collection
from backend.models import Product

products_router = APIRouter()

@products_router.get("/{product_txt}", response_model=str)
async def get_product(product_txt: str):
    regex = ".*".join(product_txt.split())
    product = products_collection.find({"name": {"$regex": regex, "$options": 'i'}})
    return product

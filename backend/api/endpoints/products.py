from fastapi import APIRouter, HTTPException
from typing import List, Optional
from database import products_collection, price_by_date_collection
from schemas import Product, Price_by_date

router = APIRouter()


@router.get("/products", response_model=List[Product])
async def get_product(search: Optional[str] = None):
    if search is None:
        raise HTTPException(status_code=404, detail="No search query provided")
    regex = ".*".join(search.split())
    query = {"name": {"$regex": regex, "$options": "i"}}
    products = []
    for product in products_collection.find(query):
        products.append(Product(**product))
    if not products:
        raise HTTPException(status_code=404, detail="No products found")
    return products


@router.get("/price-by-dates", response_model=List[Price_by_date])
async def read_price_by_dates():
    price_by_dates = []
    for price_by_date in price_by_date_collection.find():
        price_by_dates.append(Price_by_date(**price_by_date))
    return price_by_dates

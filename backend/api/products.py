from fastapi import APIRouter, HTTPException
from typing import List, Optional
from database import products_collection
from schemas import Product

products_router = APIRouter()


@products_router.get("/", response_model=List[Product])
async def get_products(search: Optional[str] = None):
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

from fastapi import APIRouter, HTTPException
from typing import Optional
from database import price_by_date_collection
from schemas import Price_by_date

price_by_date_router = APIRouter()


@price_by_date_router.get("/", response_model=Price_by_date)
async def get_price_by_date(search_id: Optional[str]):
    if search_id is None:
        raise HTTPException(status_code=404, detail="No search query provided")
    price_by_date = price_by_date_collection.find_one({"_id": search_id})
    if not price_by_date:
        raise HTTPException(status_code=404, detail="No products found")
    price_by_date = Price_by_date(**price_by_date)
    return price_by_date

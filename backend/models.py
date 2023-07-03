from pydantic import BaseModel
from typing import Optional, List


class Price(BaseModel):
    original: str
    current: str
    lowest: str


class Product(BaseModel):
    _id: str
    name: str
    brand: str
    price: Price
    large_ctg: str
    small_ctg: List[str]


class Price_by_date(BaseModel):
    _id: str
    date: str
    price: str

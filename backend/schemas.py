from pydantic import BaseModel, Field
from typing import List


class Dates(BaseModel):
    date: str
    price: int


class Price(BaseModel):
    original: int
    current: int
    lowest: int


class Product(BaseModel):
    _id: str = Field(..., alias="_id.$oid")
    name: str
    brand: str
    price: Price
    large_ctg: str
    small_ctg: List[str]


class Price_by_date(BaseModel):
    _id: str = Field(..., alias="_id.$oid")
    dates: List[Dates]

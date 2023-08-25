from pydantic import BaseModel,Field
from typing import List


class Dates(BaseModel):
    date: str
    price: int


class Price(BaseModel):
    original: int
    current: int
    lowest: int


class Product(BaseModel):
    id_: str = Field(..., alias="_id")
    name: str
    brand: str
    price: Price
    large_ctg: str
    small_ctg: List[str]


class Price_by_date(BaseModel):
    id_: str = Field(..., alias="_id")
    dates: List[Dates]

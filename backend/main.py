from fastapi import FastAPI
from api.products import products_router
from api.price_by_date import price_by_date_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://api.olivedb.info",
    "https://api.olivedb.info",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def get_names():
    return {
        "Welcom": "api.olivedb.info",
        "docs": "api.olivedb.info/docs",
        "url": {
            "Search Products": "api.olivedb.info/products?search=[name]",
            "Search Price By date": "api.olivedb.info/price-by-date?search_id=[search_id]",
        },
        "example data": {
            "_id": "A000000186966",
            "brand": "라운드랩",
            "large_ctg": "스킨케어",
            "name": "라운드랩 1025 독도 토너 500ml+200ml 기획(+소나무 클렌저 10ml 증정)",
            "price": {
                "current": 45000,
                "lowest": 29200,
                "original": 45000,
            },
            "small_ctg": ["토너/로션/올인원"],
        },
    }


app.include_router(products_router, prefix="/products")
app.include_router(price_by_date_router, prefix="/price-by-date")

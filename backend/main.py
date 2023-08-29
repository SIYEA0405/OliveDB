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
    return {"Welcom": "api.olive.db"}


app.include_router(products_router, prefix="/products")
app.include_router(price_by_date_router, prefix="/price-by-date")

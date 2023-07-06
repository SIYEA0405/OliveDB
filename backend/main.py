from fastapi import FastAPI
from api.endpoints.products import products_router

app = FastAPI()

app.include_router(products_router, prefix="/api/endpoints")


@app.get("/")
def read_root():
    return {"Hello": "World"}

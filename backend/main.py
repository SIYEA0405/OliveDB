from fastapi import FastAPI
from api.endpoints.products import router

app = FastAPI()

app.include_router(router, prefix="/api/endpoints")


@app.get("/")
def read_root():
    return {"Hello": "World"}

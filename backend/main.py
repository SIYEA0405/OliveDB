from fastapi import FastAPI
from api.products import router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://oliveDB.info",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router, prefix="/api")


@app.get("/")
def read_root():
    return {"Hello": "World"}

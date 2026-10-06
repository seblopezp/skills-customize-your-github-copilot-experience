from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Items API")

items = [
    {"id": 1, "name": "Laptop", "price": 999.99},
    {"id": 2, "name": "Mouse", "price": 25.00},
]


class Item(BaseModel):
    name: str
    price: float


@app.get("/")
def read_root():
    return {"message": "Welcome to the API"}


# TODO: Add GET /items
# TODO: Add POST /items
# TODO: Add GET /items/{item_id}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)

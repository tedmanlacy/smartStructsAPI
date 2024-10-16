from typing import Union
from pydantic import BaseModel
from fastapi import FastAPI


app = FastAPI()

class Order(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/orders/{order_id}")
def read_item(order_id: int, q: Union[str, None] = None):
    return {"order_id": order_id, "q": q}

@app.put("/orders/{order_id}")
def update_item(order_id: int, order: Order):
    return {"order_name": order.name, "order_id": order_id}
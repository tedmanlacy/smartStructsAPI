from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/oysters/{oyster_id}")
def read_item(oyster_id: int, q: Union[str, None] = None):
    return {"oyster_id": oyster_id, "q": q}
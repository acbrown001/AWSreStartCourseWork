from fastapi import FastAPI
from typing import Union 
# You can use Union to declare that a parameter can be one of several types. 
# List, Dict, Tuple, Set, etc. are all available in the typing module.
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World - change3"}


class Item(BaseModel):
    name: str
    price: float


@app.get("/items/{item_id}")
def read_item(item_id: int, item: Item, q: Union[str, None] = None): #Default value for q is None
   return {"item_id": item_id, "q": q, "item": item}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
  return {"item_id": item_id, "item": item}


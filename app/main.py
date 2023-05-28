from fastapi import FastAPI

from pydantic import BaseModel

item_master = { 1 : "This is a mango",
                2 : "This is a banana",
                3 : "This is an apple",
                4 : "This is a pineapple",
                5 : "This is a papaya",
                }

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items")
async def items():
    return {"items": item_master}

@app.get("/items/{item_id}")
async def get_item (item_id: int, short: bool):
    if short == True: 
        return {"item": item_master[item_id]}
    else:
        return {"item": "This is the long description"}

@app.post("/items")
async def create_item(item: Item):
    return item

    


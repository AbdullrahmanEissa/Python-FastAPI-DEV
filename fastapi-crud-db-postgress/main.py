from typing import Optional
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    id: int
    name: str
    description: Optional[str] = None

items = [
    Item( id=1, name="Item 1", description="This is the first item"),
    Item( id=2, name="Item 2", description="This is the second item")
]
@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/")
def read_items():
    return items

@app.get("/items/{item_id}")
def read_item(item_id: int):
    if item_id < 0 or item_id >= len(items):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    return items[item_id]

@app.post("/items/")
def create_item(item: Item):
    items.append(item)
    return item

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    if item_id < 0 or item_id >= len(items):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    items[item_id] = item
    return item

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id < 0 or item_id >= len(items):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    deleted_item = items.pop(item_id)
    return deleted_item



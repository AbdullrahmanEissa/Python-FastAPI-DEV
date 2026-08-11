from fastapi import FastAPI

app = FastAPI()

items = [
    {"id": 1, "name": "Item 1"},
    {"id": 2, "name": "Item 2"},
    {"id": 3, "name": "Item 3"}
]

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/items/")
def get_items():
    return items

# This Is A Path Parameters 

@app.get("/items/{item_id}")
def get_item(item_id: int):
    for item in items:
        if item["id"] == item_id:
            return item
    return {"error": "Item not found"}

# This Is The Querry Parameters

@app.get("/items/")
def get_items_with_query(skip: int = 0, limit: int = 10):
    return items[skip : skip + limit]
    
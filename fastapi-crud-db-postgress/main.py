from fastapi import FastAPI, HTTPException, status, Depends
from pydantic import BaseModel
from typing import Optional
from sqlalchemy.orm import Session
import models
from database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

class Item(BaseModel):
    id: int
    name: str
    description: Optional[str] = None

@app.get("/items/{item_id}", response_model=Item)
def read_item(item_id: int, db: Session = Depends(get_db)):
    item = db.query(models.Item).filter(models.Item.id == item_id).first()
    if item is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    return item

@app.get("/items", response_model=list[Item])
def read_items(db: Session = Depends(get_db)):
    items = db.query(models.Item).all()
    return items

@app.post("/items", response_model=Item, status_code=status.HTTP_201_CREATED)
def create_item(item: Item, db: Session = Depends(get_db)):
    db_item = models.Item(id=item.id, name=item.name, description=item.description)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, item: Item, db: Session = Depends(get_db )):
    db_item = db.query(models.Item).filter(models.Item.id == item_id).first()
    if db_item is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    db_item.name = item.name
    db_item.description = item.description
    db.commit()
    db.refresh(db_item)
    return db_item

@app.delete("/items/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(item_id: int, db: Session = Depends(get_db)):
    db_item = db.query(models.Item).filter(models.Item.id == item_id).first()
    if db_item is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    db.delete(db_item)
    db.commit()
    return None
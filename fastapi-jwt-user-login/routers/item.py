from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
import models, schemas, oauth2 # ( oauth for authentication and authorization )
from database import get_db

router = APIRouter(
    prefix="/items",
    tags=["Items"]
)

@router.get("/{item_id}", response_model=schemas.ItemResponse)
def read_item(item_id: int, db: Session = Depends(get_db)):
    item = db.query(models.Item).filter(models.Item.id == item_id).first()
    if item is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    return item

@router.get("/", response_model=list[schemas.ItemResponse])
def read_items(db: Session = Depends(get_db)):
    items = db.query(models.Item).all()
    return items


# ( Depends(oauth2.get_current_user)` is used to ensure that the user is authenticated before they can create, update, or delete an item. The get_current_user function in oauth2.py verifies the JWT token and retrieves the current user from the database. If the user is not authenticated, an HTTPException with a 401 status code will be raised. )`)
@router.post("/", response_model=schemas.ItemResponse, status_code=status.HTTP_201_CREATED)
def create_item(item: schemas.ItemCreate, db: Session = Depends(get_db), current_user: models.User = Depends(oauth2.get_current_user)):
    db_item = models.Item(name=item.name, description=item.description)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@router.put("/{item_id}", response_model=schemas.ItemResponse)
def update_item(item_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db), current_user: models.User = Depends(oauth2.get_current_user)):
    item_query = db.query(models.Item).filter(models.Item.id == item_id)
    db_item = item_query.first()
    if db_item is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    
    item_query.update(item.model_dump(), synchronize_session=False)
    db.commit()
    return item_query.first()

@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(item_id: int, db: Session = Depends(get_db), current_user: models.User = Depends(oauth2.get_current_user)):
    db_item = db.query(models.Item).filter(models.Item.id == item_id).first()
    if db_item is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    db.delete(db_item)
    db.commit()
    return None
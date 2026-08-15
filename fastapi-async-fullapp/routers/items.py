from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import update
import models, schemas, oauth2
from database import get_db

router = APIRouter(
    prefix="/items",
    tags=["Items"]
)

@router.get("/{item_id}", response_model=schemas.ItemResponse)
async def read_item(item_id: int, db: AsyncSession = Depends(get_db)):
    query = select(models.Item).filter(models.Item.id == item_id)
    result = await db.execute(query)
    item = result.scalars().first()
    
    if item is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    return item

@router.get("/", response_model=list[schemas.ItemResponse])
async def read_items(db: AsyncSession = Depends(get_db)):
    query = select(models.Item)
    result = await db.execute(query)
    items = result.scalars().all()
    return items

@router.post("/", response_model=schemas.ItemResponse, status_code=status.HTTP_201_CREATED)
async def create_item(item: schemas.ItemCreate, db: AsyncSession = Depends(get_db), current_user: models.User = Depends(oauth2.get_current_user)):
    db_item = models.Item(name=item.name, description=item.description)
    db.add(db_item)
    await db.commit()
    await db.refresh(db_item)
    return db_item

@router.put("/{item_id}", response_model=schemas.ItemResponse)
async def update_item(item_id: int, item: schemas.ItemCreate, db: AsyncSession = Depends(get_db), current_user: models.User = Depends(oauth2.get_current_user)):
    query = select(models.Item).filter(models.Item.id == item_id)
    result = await db.execute(query)
    db_item = result.scalars().first()
    
    if db_item is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    
    stmt = update(models.Item).where(models.Item.id == item_id).values(**item.model_dump())
    await db.execute(stmt)
    await db.commit()
    
    refresh_query = select(models.Item).filter(models.Item.id == item_id)
    refresh_result = await db.execute(refresh_query)
    return refresh_result.scalars().first()

@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_item(item_id: int, db: AsyncSession = Depends(get_db), current_user: models.User = Depends(oauth2.get_current_user)):
    query = select(models.Item).filter(models.Item.id == item_id)
    result = await db.execute(query)
    db_item = result.scalars().first()
    
    if db_item is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    
    await db.delete(db_item)
    await db.commit()
from sqlmodel import Session, select
from typing import Optional
from datetime import datetime, timezone 

from app.models.item_model import Item
from app.models.category_model import Category
from app.schemas.item_schema import CreateItem, ReadItem

def create_item(session: Session, data: CreateItem) -> ReadItem:
    existing = session.exec(
        select(Item).where(Item.name == data.name)
    ).first()
    
    if existing:
        raise ValueError("Item is already exist")
    
    category = session.exec(
        select(Category).where(Category.name == data.category_name)
    ).first()
    
    if category is None:
        raise ValueError("Category name is not available")
    
    item = Item(
        name=data.name,
        image_link=data.image_link,
        recycle=data.recycle,
        is_reusable=data.is_reusable,
        is_recyclable=data.is_recyclable,
        is_hazardous=data.is_hazardous,
        category_id=category.id
    )
    
    session.add(item)
    session.commit()
    session.refresh(item)
    
    return item    

def show_item(session: Session, name: Optional[str], ):
    statement = select(Item)
    
    if name:
        statement = statement.where(
            Item.name.ilike(f"%{name}%")
        )
        
    return session.exec(statement).all()


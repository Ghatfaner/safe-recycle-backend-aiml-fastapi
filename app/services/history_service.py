from sqlmodel import Session, func, select, desc
from typing import Optional, List
from datetime import datetime, timezone, timedelta

from app.models.history_model import History
from app.models.item_model import Item
from app.schemas.history_schema import CreateHistory, PopularItem

def create_history(session: Session, data: CreateHistory):   
    history = History(
        user_id=data.user_id,
        item_id=data.item_id
    ) 
    
    session.add(history)
    session.commit()

def get_popular_items(session: Session):
    
    seven_days_history = datetime.now(timezone.utc) - timedelta(days=7)

    statement = (
        select(Item, func.count(History.id).label("popularity_count"))
        .join(History, Item.id == History.item_id)
        .where(History.viewed_at >= seven_days_history)
        .group_by(Item.id)
        .order_by(desc("popularity_count"))
        .limit(10)
    )

    results = session.exec(statement).all()

    popular_items = [row[0] for row in results]

    return popular_items
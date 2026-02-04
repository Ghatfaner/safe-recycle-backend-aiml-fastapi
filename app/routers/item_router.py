from uuid import uuid4
from sqlmodel import Session
from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, Query, UploadFile, File, Form
from pathlib import Path

from app.services.item_service import create_item
from app.schemas.item_schema import ReadItem, CreateItem
from app.databases.session import get_session

BASE_STORAGE = Path("storage/image/items")
BASE_STORAGE.mkdir(parents=True, exist_ok=True)

router = APIRouter(prefix="/items", tags=["item"])

@router.post("/", response_model=ReadItem, status_code=201)
def create_item_endpoint(
    name: str = Form(...),
    description: str = Form(...),
    image: UploadFile = File(),
    recycle: str = Form(...),
    is_reusable: bool = Form(...),
    is_recyclable: bool = Form(...),
    is_hazardous: bool = Form(...),
    session: Session = Depends(get_session)
):
    try:
        if image.content_type not in ["image/png", "image/jpg", "image/jpeg"]:
            raise HTTPException(400, "Invalid image type")
        
        filename = f"{uuid4().hex}_{image.filename}"
        filepath = BASE_STORAGE / filename
        
        with open(filepath, "wb") as f:
            f.write(image.file.read())
            
        item = create_item(
            session=session,
            data=CreateItem(
                name=name,
                description=description,
                recycle=recycle,
                image_link=str(filepath),
                is_reusable=is_reusable,
                is_recyclable=is_recyclable,
                is_hazardous=is_hazardous
            )
        )
        
        return item
    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )
        

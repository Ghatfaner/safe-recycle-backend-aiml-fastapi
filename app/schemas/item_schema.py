from pydantic import BaseModel
from datetime import datetime

from app.schemas.category_schema import ReadCategory

class CreateItem(BaseModel):
    name: str
    description: str
    image_link: str
    recycle: str
    
    is_reusable: bool
    is_recyclable: bool
    is_hazardous: bool
    
    category_name: str
    
class ReadItem(BaseModel):
    id: int
    name: str
    description: str
    image_link: str
    recycle: str
    
    is_reusable: bool
    is_recyclable: bool
    is_hazardous: bool
    
    category: ReadCategory
    
    model_config = {
        "from_attributes": True
    }
    
class UpdateItem(BaseModel):
    name: str
    description: str
    image_link: str
    recycle: str
    
    is_reusable: bool
    is_recyclable: bool
    is_hazardous: bool
    
    updated_at: datetime
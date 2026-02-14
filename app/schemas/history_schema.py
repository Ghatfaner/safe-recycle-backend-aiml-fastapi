from pydantic import BaseModel, ConfigDict
from sqlmodel import SQLModel
from typing import List
from app.schemas.base_response_schema import BaseResponse

class CreateHistory(BaseModel):
    user_id: int
    item_id: int

class PopularItem(BaseModel):
    id: int
    name: str
    image_link: str
    category_id: int

    model_config = ConfigDict(from_attributes=True)

class ResponsePopularItem(BaseResponse):
    data: List[PopularItem]
from pydantic import BaseModel
from typing import List

from app.schemas.base_response_schema import BaseResponse

class CreateHistory(BaseModel):
    user_id: int
    item_id: int

class Recommendations(BaseModel):
    item_id: int
    item_name: str
    item_category: str
    item_image_link: str    
    
class ResponseRecommendations(BaseResponse):
    data: List[Recommendations]
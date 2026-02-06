from fastapi import UploadFile
from pydantic import BaseModel

class LLMRequest(BaseModel):
    
    id: int
    image_filename: str
    model_name: str
    prompt: str
    output_message: str
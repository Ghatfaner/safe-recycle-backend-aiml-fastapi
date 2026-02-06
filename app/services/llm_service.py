import os
import tempfile
import shutil
import requests

from fastapi import UploadFile
from google import genai
from google.genai import types
from sqlmodel import Session

from app.core.config import settings
from app.schemas.llm_schema import LLMRequest
from app.models.llm_model import LLMModel


async def process_llm_request(model_name: str, prompt: str, upload_file: UploadFile, session: Session) -> LLMModel:

    client = genai.Client(api_key=settings.GEMINI_API_KEY)

    temp_file_path = None

    try:
        
        image_bytes = await upload_file.read()
        mime_type = upload_file.content_type or "image/jpeg" or "image/jpg"

        response = client.models.generate_content(
            model=model_name,
            contents=[
                prompt,
                types.Part.from_bytes(
                    data=image_bytes,
                    mime_type=mime_type
                )
            ]
        )

        return response.text

    except Exception as e:
        print(f"Error processing uploaded file: {str(e)}")
        raise e
    
    finally:
        if temp_file_path:
            os.unlink(temp_file_path)

# with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmp :
        #     shutil.copyfileobj(upload_file.file, tmp)
        #     temp_file_path = tmp.name

        # with open(temp_file_path, "rb") as f :
        #     image_bytes = f.read()

        # image_part = types.Part.from_bytes(
        #     data=image_bytes,
        #     mime_type="image/jpg, image/jpeg"
        # )

        # my_file = client.files.upload(image_part)


        # response = client.models.generate_content(
        #     model=llm_request.model_name,
        #     contents=["Describe the image in detail in one short paragraph (3-5 phrases or sentences)", my_file]
        # )

        # return response.text
from fastapi import FastAPI 
from replicate_ai.main import *
from pydantic import BaseModel

router = FastAPI()

class Prompt(BaseModel):
    prompt: str
    
@router.get('/')
async def main():
    return {
        "Message" : "Hello!"
    }
    
@router.post('/photo/')
async def text_photo(request: Prompt):
    a = text_to_photo(prompt=request.prompt)
    return {
        "image_url" : await a
    }
    
@router.post('/video')
async def text_video(request: Prompt):
    a = text_to_video(prompt = request.prompt)
    return {
        "video_url" : await a
    }
@router.post('/text')
async def text_text(request: Prompt):
    a = text_to_text(prompt=request.prompt)
    return {
        "output" : await a
    }    
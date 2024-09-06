from pydantic import BaseModel
from typing import List, Dict

# Request body model
class ChatRequest(BaseModel):
    input_text: str

# Response model
class ChatResponse(BaseModel):
    text: str
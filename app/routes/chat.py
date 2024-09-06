from app.utils.model import get_memory,get_chat_response
from fastapi import APIRouter,HTTPException,FastAPI,Request,Cookie
from typing import List, Dict
from app.src.schema import ChatRequest,ChatResponse
import requests
import logging

session = requests.Session()
session.cache_disabled = True


# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

memory = get_memory()
chat_history = []  # Chat history in memory

router = APIRouter()



@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    try:
        input_text = request.input_text
       
        # Append the user's message to the chat history
        chat_history.append({"role": "user", "text": input_text})
        # Generate the chatbot's response
        chat_response = get_chat_response(input_text=input_text, memory=memory)
        print(f"response:{chat_response}")
        #  Append the chatbot's response to the chat history
        chat_history.append({"role": "assistant", "text": chat_response})
        return {"text": chat_response}
    except Exception as e:
        logger.error(f"An error occurred: {e}")
        raise HTTPException(status_code=500, detail=str(e))
    

@router.post("/clear")
async def clear_chat():
    global chat_history
    chat_history = []
    memory.clear()
    logger.info("cleared history")
    return {"message":"chat history cleared"}
    

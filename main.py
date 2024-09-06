from fastapi import FastAPI, Request,Cookie,Response
from fastapi.middleware.cors import CORSMiddleware
from app.routes import chat
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import uvicorn
import uuid

app = FastAPI()

# Allow CORS for frontend interaction
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Include routes
app.include_router(chat.router,prefix="/bot", tags=["Chatbot"])

# Serve static files (CSS, JS)

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def get(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


# @app.get("/", response_class=HTMLResponse)
# async def get(response:Response,session_id:str =Cookie(None)):
#     if session_id is None:
#         session_id = str(uuid.uuid4())
#         response.set_cookie(key="session_id",value=session_id)
#     with open("templates/index.html") as f:
#         return HTMLResponse(f.read(),status_code=200)

# app.mount("/", StaticFiles(directory="frontend"), name="frontend")

if __name__ == "__main__":
    uvicorn.run(app,host="127.0.0.1",port=8000)


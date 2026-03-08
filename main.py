from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import agent_service

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Message(BaseModel):
    message: str
@app.post("/chat")
def chat(msg: Message):
    try:
        response = agent_service.agent(msg.message)
        return {"response": response}
    except Exception as e:
        print(f"Server Error: {e}")
        return {"response": "מצטער, חלה שגיאה בשרת. אנא נסה שוב מאוחר יותר."}

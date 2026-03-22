from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from agents.career_agent import run_career_agent
from config.settings import PROJECT_NAME

app = FastAPI(title=PROJECT_NAME)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class UserInput(BaseModel):
    message: str
    user_id: str = "default_user"


@app.get("/")
def home():
    return {"message": f"{PROJECT_NAME} is running."}


@app.post("/career-guide/")
def career_guide(data: UserInput):
    return run_career_agent(data.message, data.user_id)
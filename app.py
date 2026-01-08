from fastapi import FastAPI
from pydantic import BaseModel
from react_agent import run_agent

app = FastAPI()

class UserInput(BaseModel):
    message: str

@app.post("/chat")
def chat(user_input: UserInput):
    return {"response": run_agent(user_input.message)}

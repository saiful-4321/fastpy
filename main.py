from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello world"}

@app.post("/createposts")
def createposts(payload: dict = Body(...)):
    return payload

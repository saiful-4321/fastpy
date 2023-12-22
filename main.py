from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello world"}


class Post(BaseModel):
    title: str
    content: str

@app.post("/createposts")
def createposts(post: Post):
    print(post)
    return {"data": post}

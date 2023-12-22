from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello world"}


class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

@app.post("/createposts")
def createposts(post: Post):
    print(post.rating)
    print(post.dict())
    return {"data": post}

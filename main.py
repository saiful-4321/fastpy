from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

all_posts = [
    {
        "id": 1,
        "title": "Title for post 1",
        "content": "Content of post 1",
        "published": True
    },
    {
        "id": 2,
        "title": "Title for post 2",
        "content": "Content of post 2",
        "published": False
    },
]

@app.get("/")
async def root():
    return {"message": "Hello world"}
class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

@app.get("/posts")
def get_posts():
    return {'data': all_posts}

@app.post("/posts")
def createposts(post: Post):
    print(post.rating)
    print(post.dict())
    return {"data": post}

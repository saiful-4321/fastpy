from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange

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

@app.get("/posts")
def get_posts():
    return {'data': all_posts}
class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

@app.post("/posts")
async def createposts(post: Post):
    post_dict = post.dict()
    post_dict['id'] = randrange(0, 10000000)
    all_posts.append(post_dict)
    return {'data': all_posts}

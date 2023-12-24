from fastapi import FastAPI, Response, status, HTTPException
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

@app.post("/posts", status_code=status.HTTP_201_CREATED)
async def createposts(post: Post):
    post_dict = post.dict()
    post_dict['id'] = randrange(0, 10000000)
    all_posts.append(post_dict)
    return {'data': all_posts}

def find_post(id):
    for post in all_posts:
        if post['id'] == id:
            return post

@app.get("/post/latest")
async def get_latest_post():
    post = all_posts[len(all_posts)-1]
    return {"Post": post}

@app.get("/posts/{id}")
async def get_post(id: int, response: Response):
    post = find_post(id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with Id: {id} was not found")
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"message": f"post with Id: {id} was not found"}
    return {"post": post}

def find_index_post(id: int):
    for index, post in enumerate(all_posts):
        if post['id'] == id:
            return index

@app.delete("/posts/{id}")
async def delete_post(id: int):
    index = find_index_post(id=id)
    all_posts.pop(index)
    return {'message': 'Post successfully removed'}
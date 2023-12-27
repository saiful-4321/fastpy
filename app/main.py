from fastapi import FastAPI, Response, status, HTTPException, Depends
from sqlalchemy.orm import Session 
# from fastapi.params import Body
from typing import Optional
from pydantic import BaseModel
from .models.Post import Post
from .database import Base, engine, get_db
Base.metadata.create_all(bind=engine)

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

@app.get("/posts")
def get_posts(db: Session = Depends(get_db)):
    posts = db.query(Post).all()
    return {'data': posts}

class PostSchema(BaseModel):
    title: str
    content: str
    is_published: bool = True

@app.post("/posts", status_code=status.HTTP_201_CREATED)
async def create_posts(post: PostSchema, db: Session = Depends(get_db)):
    new_post = Post(**post.model_dump())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return {'data': new_post}

def find_post(id):
    for post in all_posts:
        if post['id'] == id:
            return post

# @app.get("/post/latest")
# async def get_latest_post():
#     post = all_posts[len(all_posts)-1]
#     return {"Post": post}

# @app.get("/posts/{id}")
# async def get_post(id: int, response: Response):
#     post = find_post(id)
#     if not post:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with Id: {id} was not found")
#         # response.status_code = status.HTTP_404_NOT_FOUND
#         # return {"message": f"post with Id: {id} was not found"}
#     return {"post": post}

# def find_index_post(id: int):
#     for index, post in enumerate(all_posts):
#         if post['id'] == id:
#             return index

# @app.delete("/posts/{id}")
# async def delete_post(id: int):
#     index = find_index_post(id=id)
#     if index == None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with that id: {id} does not exists")
#     all_posts.pop(index)
#     return {'message': 'Post successfully removed'}

# @app.put("/posts/{id}")
# def update_post(id: int, post: Post):
#     index = find_index_post(id)
#     if index == None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id: {id} does not exists")
    
#     post_dict = post.dict()
#     post_dict['id'] = id
#     all_posts[index] = post_dict
#     return {'data': post_dict}
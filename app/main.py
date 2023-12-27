from fastapi import FastAPI, status, HTTPException, Depends
from sqlalchemy.orm import Session 
from .models.Post import Post
from .database import Base, engine, get_db
from .schemas import PostSchema
Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/posts")
def get_posts(db: Session = Depends(get_db)):
    try: 
        posts = db.query(Post).all()
        return {'data': posts}
    except Exception as ex:
        print(f"An error occurred: {ex}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An error occurred: {str(ex)}"
        )

@app.post("/posts", status_code=status.HTTP_201_CREATED)
async def create_posts(post: PostSchema, db: Session = Depends(get_db)):
    try: 
        new_post = Post(**post.model_dump())
        db.add(new_post)
        db.commit()
        db.refresh(new_post)
        return {'data': new_post}
    except Exception as ex:
        db.rollback()
        print(f"An error occurred: {ex}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An error occurred: {str(ex)}"
        )

@app.get("/posts/{id}")
async def get_post(id: int, db: Session = Depends(get_db)):
    try:
        post = db.query(Post).filter(Post.id == id).first()
        
        if not post:
            return {"message": f"Post with ID {id} not found", "data": {}}
        
        return {"message": "Success", "data": post}
    except Exception as ex:
        print(f"An error occurred: {ex}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An error occurred: {str(ex)}"
        )

@app.delete("/posts/{id}")
async def delete_post(id: int, db: Session = Depends(get_db)):
    try: 
        post = db.query(Post).filter(Post.id == id)
        if post.first() is None:
            return {"message": f"Post with ID {id} not found", "data": {}}
        
        post.delete(synchronize_session=False)
        db.commit()
        return {'message': 'Post successfully removed'}
    except Exception as ex:
        db.rollback()
        print(f"An error occurred: {ex}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An error occurred: {str(ex)}"
        )

@app.put("/posts/{id}")
def update_post(id: int, post: PostSchema, db: Session=Depends(get_db)):
    try: 
        post_query = db.query(Post).filter(Post.id == id)
        if post_query.first() is None:
            return {"message": f"Post with ID {id} not found", "data": {}}
        
        post_query.update(post.model_dump(), synchronize_session=False)
        db.commit()
        return {'message': 'Post successfully Updated', 'data': post_query.first()}
    except Exception as ex:
        db.rollback()
        print(f"An error occurred: {ex}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An error occurred: {str(ex)}"
        )
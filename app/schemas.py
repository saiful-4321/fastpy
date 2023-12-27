from pydantic import BaseModel

class PostBase(BaseModel):
    title: str
    content: str
    is_published: bool = True

class PostCreate(PostBase):
    pass

class PostUpdate(PostBase):
    is_published: bool
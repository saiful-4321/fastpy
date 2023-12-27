from pydantic import BaseModel

class PostSchema(BaseModel):
    title: str
    content: str
    is_published: bool = True
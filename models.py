from pydantic import BaseModel, EmailStr


class Post(BaseModel):
    title: str
    content: str
    author_email: EmailStr


class Comment(BaseModel):
    post_id: str 
    commenter_name: str
    content: str





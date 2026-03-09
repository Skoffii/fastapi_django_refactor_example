from pydantic import BaseModel
from datetime import datetime


class Comment(BaseModel):
    text: str
    post_id: int
    created_at: datetime
    author_id: int


class CommentRequest(BaseModel):
    pass


class CommentUpdate(BaseModel):
    text: str | None = None


class CommentResponse(Comment):
    pass

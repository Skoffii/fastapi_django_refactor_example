from pydantic import BaseModel
from datetime import datetime
from users import User

from posts import Post


class Comment(BaseModel):
    text: str
    post: int = Post.id
    created_at: datetime
    author: int = User.id

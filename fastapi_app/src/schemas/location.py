from pydantic import BaseModel, Field


class Location(BaseModel):
    is_published: bool = True
    name: str = Field(max_length=256)

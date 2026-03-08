from pydantic import BaseModel, SecretStr, ConfigDict


class User(BaseModel):
    id: int
    model_config = ConfigDict(from_attributes=True)
    login: str
    Email: str
    full_name: str | None


class UserCreate(User):
    password: SecretStr

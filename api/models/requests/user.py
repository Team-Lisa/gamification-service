from pydantic.main import BaseModel

class User(BaseModel):
    email: str

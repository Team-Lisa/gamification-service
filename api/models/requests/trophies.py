from pydantic.main import BaseModel

class Trophy(BaseModel):
    description: str
    points: int

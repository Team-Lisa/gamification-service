from pydantic.main import BaseModel

class Trophy(BaseModel):
    customId: int
    description: str
    points: int

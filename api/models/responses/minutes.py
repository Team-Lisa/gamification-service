from pydantic.main import BaseModel


class Minutes(BaseModel):
    extra_minutes: int
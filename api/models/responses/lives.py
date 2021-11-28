from pydantic.main import BaseModel


class Lives(BaseModel):
    lives: int
    last_life_actualization: str
    actual_time: str
    won_trophies: list
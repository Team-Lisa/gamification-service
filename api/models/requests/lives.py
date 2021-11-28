from typing import Optional

from pydantic.main import BaseModel


class Lives(BaseModel):
    lives: int #un numero positivo sumara vidas, mientras que un numero negativo las restara
    market: Optional[bool] = False
from pydantic.main import BaseModel


class Points(BaseModel):
    points: int #un numero positivo sumara puntos, mientras que un numero negativo los restara
from pydantic.main import BaseModel


class StoreItems(BaseModel):
    items: list
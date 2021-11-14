from pydantic.main import BaseModel


class UserStatus(BaseModel):
    user_status: dict
    actual_time: str
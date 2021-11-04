from fastapi import APIRouter
from api.controllers.gamification_controller import GamificationController
from api.models.responses.trophies import Trophies as TrophiesResponse
from api.models.responses.user import UserStatus as UserStatusResponse
from api.models.requests.user  import User

router = APIRouter(tags=["Users"])

@router.get("/users", response_model=UserStatusResponse)
async def get_user_status(email: str = ""):
    return GamificationController.get_user_status_by_email(email)


@router.post("/users", response_model=UserStatusResponse)
async def post_user_status(user:User):
    return GamificationController.create_user_status(user)
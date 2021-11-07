from fastapi import APIRouter
from api.controllers.gamification_controller import GamificationController
from api.models.responses.trophies import Trophies as TrophiesResponse
from api.models.responses.lives import Lives as LivesResponse
from api.models.requests.lives import Lives as LivesRequest
from api.models.requests.user  import User

router = APIRouter(tags=["Lives"])

@router.get("/lives", response_model=LivesResponse)
async def get_user_lives(email: str = ""):
    return GamificationController.get_user_lives_by_email(email)


@router.patch("/lives", response_model=LivesResponse)
async def update_user_lives(lives: LivesRequest,email: str = ""):
    return GamificationController.update_user_lives(email,lives)

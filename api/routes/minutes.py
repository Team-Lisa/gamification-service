from fastapi import APIRouter
from api.controllers.gamification_controller import GamificationController
from api.models.responses.minutes import Minutes as MinutesResponse
from api.models.requests.minutes import Minutes as MinutesRequest


router = APIRouter(tags=["Minutes"])

@router.get("/minutes", response_model=MinutesResponse)
async def get_user_minutes(email: str = ""):
    return GamificationController.get_user_minutes_by_email(email)


@router.patch("/minutes", response_model=MinutesResponse)
async def update_user_minutes(points: MinutesRequest,email: str = ""):
    return GamificationController.update_user_minutes(email,points)

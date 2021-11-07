from fastapi import APIRouter
from api.controllers.gamification_controller import GamificationController
from api.models.responses.points import Points as PointsResponse
from api.models.requests.points import Points as PointsRequest


router = APIRouter(tags=["Points"])

@router.get("/points", response_model=PointsResponse)
async def get_user_points(email: str = ""):
    return GamificationController.get_user_points_by_email(email)


@router.patch("/points", response_model=PointsResponse)
async def update_user_points(points: PointsRequest,email: str = ""):
    return GamificationController.update_user_points(email,points)

from fastapi import APIRouter
from api.controllers.gamification_controller import GamificationController
from api.models.responses.fastforwards import Fastforwards as FastforwardsResponse
from api.models.requests.fastforwards import Fastforwards as FastforwardsRequest
from api.models.responses.wonTrophies import WonTrophies

router = APIRouter(tags=["Fastforwards"])

@router.get("/fastforwards", response_model=FastforwardsResponse)
async def get_user_fastforwards(email: str = ""):
    return GamificationController.get_user_fastforwards_by_email(email)


@router.patch("/fastforwards", response_model=WonTrophies)
async def update_user_fastforwards(amount: FastforwardsRequest,email: str = ""):
    return GamificationController.update_user_fastforwards(email,amount)
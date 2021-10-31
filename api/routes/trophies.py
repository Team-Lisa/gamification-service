from fastapi import APIRouter
from api.controllers.gamification_controller import GamificationController
from api.models.responses.trophies import Trophies as TrophiesResponse
from api.models.requests.trophies import Trophy


router = APIRouter(tags=["Trophies"])


@router.get("/trophies", response_model=TrophiesResponse)
async def get_trophies():
    return GamificationController.get_trophies()


@router.post("/trophies")
async def post_trophy(trophy:Trophy):
    return GamificationController.create(trophy)






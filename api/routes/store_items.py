from fastapi import APIRouter
from api.controllers.gamification_controller import GamificationController
from api.models.responses.store_items import StoreItems as StoreItemsResponse
from api.models.requests.trophies import Trophy


router = APIRouter(tags=["StoreItems"])


@router.get("/storeitems", response_model=StoreItemsResponse)
async def get_store_items():
    return GamificationController.get_store_items()

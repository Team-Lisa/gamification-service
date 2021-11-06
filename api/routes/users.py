from fastapi import APIRouter
from api.controllers.gamification_controller import GamificationController
from api.models.requests.unit import Unit
from api.models.responses.message import Message
from api.models.responses.units import Units as UnitsResponse
from api.models.responses.unit import Unit as UnitResponse
from api.models.responses.user import UserStatus as UserStatusResponse
from api.models.requests.user  import User

router = APIRouter(tags=["Users"])

@router.get("/users", response_model=UserStatusResponse)
async def get_user_status(email: str = ""):
    return GamificationController.get_user_status_by_email(email)


@router.post("/users", response_model=UserStatusResponse)
async def post_user_status(user:User):
    return GamificationController.create_user_status(user)


@router.get("/users/history/challenges/{challenge_id}", response_model=UnitsResponse) #obtengo todas las unidades del challenge
async def get_user_history_units_of_a_challenge(challenge_id: str,email: str = ""):
    return GamificationController.get_units_of_a_challenge(challenge_id,email)

@router.get("/users/history/challenges/{challenge_id}/units/{unit_id}", response_model=UnitResponse) #obtengo cierta unidad del challenge
async def get_user_history_certain_unit_of_a_challenge(challenge_id: str,unit_id:str,email: str = ""):
    return GamificationController.get_certain_unit_of_a_certain_challenge(challenge_id,unit_id,email)

@router.patch("/users/history/challenges/{challenge_id}/units/{unit_id}", status_code=201, response_model=Message) #obtengo cierta unidad del challenge
async def update_unit_info(unit:Unit,challenge_id: str,unit_id:str,email: str = ""):
    return GamificationController.update_unit_info(unit,challenge_id,unit_id,email)

@router.patch("/users/history/challenges/{challenge_id}", status_code=201, response_model=Message) #obtengo cierta unidad del challenge
async def update_challenge_completed(challenge_id: str,email: str = ""):
    return GamificationController.update_challenge_completed(challenge_id,email)

@router.patch("/users/thropies/{trophy_id}", status_code=201, response_model=Message) #obtengo cierta unidad del challenge
async def update_challenge_completed(trophy_id: str,email: str = ""):
    return GamificationController.update_throphy_completed(trophy_id,email)
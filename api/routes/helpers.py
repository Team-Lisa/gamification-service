from fastapi import APIRouter
from api import __version__

router = APIRouter(tags=["Helpers"])


@router.get("/")
async def ping():
    return {"message": "ping"}


@router.get("/version")
async def version():
    return {"version": __version__}

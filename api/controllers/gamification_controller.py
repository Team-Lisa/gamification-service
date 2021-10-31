from api.Repositories.trophy_repository import TrophyRepository
from fastapi import HTTPException
import json

from api.models.trophy import Trophy


class GamificationController:

    @staticmethod
    def get_trophies():
        result = TrophyRepository.get_all_trophies()
        result = map(lambda trophy: trophy.convert_to_json(), list(result))
        return {"trophies": list(result)}

    @staticmethod
    def create(trophy):
        trophy = Trophy(customId=trophy.customId,description=trophy.description,points=trophy.points)
        result = TrophyRepository.add_trophy(trophy)
        return {"trophy": result.convert_to_json()}


    @staticmethod
    def find_by(value):
        raise HTTPException(status_code=404, detail="Not implemented")
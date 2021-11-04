from api.Repositories.trophy_repository import TrophyRepository
from api.controllers.constants import *
from fastapi import HTTPException
import json
from datetime import datetime

from api.Repositories.user_status_repository import UserStatusRepository
from api.models.user_status import UserStatus
from api.models.trophy import Trophy


class GamificationController:

    @staticmethod
    def get_trophies():
        result = TrophyRepository.get_all_trophies()
        result = map(lambda trophy: trophy.convert_to_json_with_id(), list(result))
        return {"trophies": list(result)}

    @staticmethod
    def create(trophy):
        trophy = Trophy(description=trophy.description,points=trophy.points)
        result = TrophyRepository.add_trophy(trophy)
        return {"trophy": result.convert_to_json_with_id()}

    @staticmethod
    def create_user_status(user):
        actual_time = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
        user_status = UserStatus(email = user.email,lives= LIVES, last_life_actualization = actual_time, actual_time = actual_time, trophies = TROPHIES, history = HISTORY, extra_minutes = EXTRA_MINUTES, fast_forward_exam = FAST_FORWARD_EXAM, points = POINTS )
        result = UserStatusRepository.add_user_status(user_status)
        return {"user_status": result.convert_to_json()}


    @staticmethod
    def get_user_status_by_email(email):
        result = UserStatusRepository.get_user_status_by_email(email)
        return {"user_status": result[0].convert_to_json()}

    @staticmethod
    def get_user_lives_by_email(email):
        result = UserStatusRepository.get_user_status_by_email(email)
        return {
            "lives": result[0]["lives"],
            "last_life_actualization": result[0]["last_life_actualization"],
            "actual_time": result[0]["actual_time"]
        }

    @staticmethod
    def update_user_lives(email, lives):
        actual_lives = GamificationController.get_user_lives_by_email(email)
        new_lives = actual_lives["lives"] + lives.lives
        result = UserStatusRepository.update_user_lives(email, new_lives)
        return {
            "lives": result[0]["lives"],
            "last_life_actualization": result[0]["last_life_actualization"],
            "actual_time": result[0]["actual_time"]
        }


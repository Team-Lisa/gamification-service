from api.Repositories.store_items_repository import StoreItemsRepository
from api.Repositories.trophy_repository import TrophyRepository
from api.controllers.constants import *
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
        time = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
        user_status = UserStatus(email = user.email,lives= LIVES, last_life_actualization = time, trophies = TROPHIES, history = HISTORY, extra_minutes = EXTRA_MINUTES, fast_forward_exam = FAST_FORWARD_EXAM, points = POINTS )
        result = UserStatusRepository.add_user_status(user_status)
        return {"user_status": result.convert_to_json()}


    @staticmethod
    def get_user_status_by_email(email):
        result = UserStatusRepository.get_user_status_by_email(email)
        return {"user_status": result[0].convert_to_json()}

    @staticmethod
    def get_user_lives_by_email(email):
        result = UserStatusRepository.get_user_status_by_email(email)
        actual_time = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
        return {
            "lives": result[0]["lives"],
            "last_life_actualization": result[0]["last_life_actualization"],
            "actual_time": actual_time
        }

    @staticmethod
    def update_user_lives(email, lives):
        actual_lives = GamificationController.get_user_lives_by_email(email)
        new_lives = actual_lives["lives"] + lives.lives
        result = UserStatusRepository.update_user_lives(email, new_lives)
        actual_time = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
        return {
            "lives": result[0]["lives"],
            "last_life_actualization": result[0]["last_life_actualization"],
            "actual_time": actual_time
        }

    @staticmethod
    def get_user_points_by_email(email):
        result = UserStatusRepository.get_user_status_by_email(email)
        return {
            "points": result[0]["points"]
        }

    @staticmethod
    def update_user_points(email, points):
        actual_points = GamificationController.get_user_status_by_email(email)
        new_points = actual_points["user_status"]["points"]+ points.points
        result = UserStatusRepository.update_user_points(email, new_points)
        return {
            "points": result[0]["points"]
        }

    @staticmethod
    def get_user_minutes_by_email(email):
        result = UserStatusRepository.get_user_status_by_email(email)
        return {
            "extra_minutes": result[0]["extra_minutes"]
        }

    @staticmethod
    def update_user_minutes(email, minutes):
        actual_minutes = GamificationController.get_user_status_by_email(email)
        new_minutes = actual_minutes["user_status"]["extra_minutes"] + minutes.extra_minutes
        result = UserStatusRepository.update_user_minutes(email, new_minutes)
        return {
            "extra_minutes": result[0]["extra_minutes"]
        }

    @staticmethod
    def get_user_fastforwards_by_email(email):
        result = UserStatusRepository.get_user_status_by_email(email)
        return {
            "fastforwards": result[0]["fast_forward_exam"]
        }

    @staticmethod
    def update_user_fastforwards(email, amount):
        actual_amount = GamificationController.get_user_status_by_email(email)
        new_amount = actual_amount["user_status"]["fast_forward_exam"] + amount.fastforwards
        result = UserStatusRepository.update_user_fastforwards(email, new_amount)
        return {
            "fastforwards": result[0]["fast_forward_exam"]
        }

    @staticmethod
    def get_store_items():
        result = StoreItemsRepository.get_all_items()
        result = map(lambda item: item.convert_to_json_with_id(), list(result))
        return {"items": list(result)}


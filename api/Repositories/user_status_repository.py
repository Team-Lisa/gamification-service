from datetime import datetime

from api.models.trophy import Trophy
from api.Repositories.db import DataBase
from api.models.user_status import UserStatus


class UserStatusRepository():

    @staticmethod
    def delete_all_users_status():
        UserStatus.objects().delete()

    @staticmethod
    def add_user_status(userStatus):
        return userStatus.save()

    @staticmethod
    def get_user_status_by_email(email):
        return UserStatus.objects(email=email)

    @staticmethod
    def update_user_lives(email ,new_lives):
        UserStatus.objects(email=email).update(lives=new_lives,last_life_actualization = datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))
        return UserStatusRepository.get_user_status_by_email(email)

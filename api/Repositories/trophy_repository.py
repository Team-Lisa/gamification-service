from api.models.trophy import Trophy
from api.Repositories.db import DataBase


class TrophyRepository():
    #
    # @staticmethod
    # def add_user(user):
    #     return user.save()
    #
    # @staticmethod
    # def get_user_by_name(value):
    #     user = User.objects(name=value)
    #     return user
    #
    @staticmethod
    def delete_all_trophies():
        Trophy.objects().delete()

    @staticmethod
    def get_all_trophies():
        return Trophy.objects()

    @staticmethod
    def add_trophy(trophy):
        return trophy.save()
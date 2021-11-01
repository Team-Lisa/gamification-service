from api.models.trophy import Trophy
from api.Repositories.db import DataBase


class TrophyRepository():

    @staticmethod
    def delete_all_trophies():
        Trophy.objects().delete()

    @staticmethod
    def get_all_trophies():
        return Trophy.objects()

    @staticmethod
    def add_trophy(trophy):
        return trophy.save()
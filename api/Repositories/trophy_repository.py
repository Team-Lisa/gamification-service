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

    @staticmethod
    def get_trophy_by_description(key):
        return Trophy.objects(despcrition=key)

    @staticmethod
    def get_trophy_by_id(id):
        return Trophy.objects.get(id = id)

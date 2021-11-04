import mongoengine
from mongoengine import Document


class UserStatus(Document):
    email = mongoengine.StringField()
    lives = mongoengine.IntField()
    last_life_actualization = mongoengine.StringField() # utlima vez que se actualizo la vida
    actual_time = mongoengine.StringField() # enviar hora actual del servidor
    trophies = mongoengine.ListField()
    history = mongoengine.DictField()
    extra_minutes = mongoengine.IntField()
    fast_forward_exam = mongoengine.IntField()
    points = mongoengine.IntField()

    def convert_to_json(self):
        result = self.to_mongo().to_dict()
        if "_id" in result:
            del result["_id"]
        return result

    def convert_to_json_with_id(self):
        result = self.to_mongo().to_dict()
        if "_id" in result:
            result["id"] = str(result["_id"])
            del result["_id"]
        return result
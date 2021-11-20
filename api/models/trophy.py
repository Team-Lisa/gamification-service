import mongoengine
from mongoengine import Document


class Trophy(Document):
    description = mongoengine.StringField()
    points = mongoengine.IntField()
    rules = mongoengine.DictField()

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
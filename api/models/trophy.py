import mongoengine
from mongoengine import Document


class Trophy(Document):
    customId = mongoengine.IntField()
    description = mongoengine.StringField()
    points = mongoengine.IntField()

    def convert_to_json(self):
        result = self.to_mongo().to_dict()
        if "_id" in result:
            del result["_id"]
        return result
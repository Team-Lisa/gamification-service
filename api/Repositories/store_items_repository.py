from api.models.store_item import StoreItem

class StoreItemsRepository():

    @staticmethod
    def delete_all_items():
        StoreItem.objects().delete()

    @staticmethod
    def get_all_items():
        return StoreItem.objects()

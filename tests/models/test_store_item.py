from api.models.store_item import StoreItem


def test_model_to_json():
    customId = 1
    description = "soy un trofeo"
    points = 200
    item = StoreItem(description=description, points=points)
    assert item.convert_to_json() == {
        "description": description,
        "points": points
    }

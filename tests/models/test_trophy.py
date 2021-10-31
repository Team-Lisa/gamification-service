from api.models.trophy import Trophy


def test_model_to_json():
    customId = 1
    description = "soy un trofeo"
    points = 200
    trophy = Trophy(customId=customId, description=description, points=points)
    assert trophy.convert_to_json() == {
        "customId": customId,
        "description": description,
        "points": points
    }

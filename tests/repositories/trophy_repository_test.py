from api.Repositories.trophy_repository import TrophyRepository
from api.models.trophy import Trophy


def test_add_user_successfully(init):
    customId = 1
    description = "soy un trofeo"
    points = 200
    result = TrophyRepository.add_trophy(Trophy(customId=customId, description=description, points=points))
    assert result.customId == customId
    assert result.description == description
    assert result.points == points

def test_get_all_trophies_successfully(init):
    customId = 1
    description = "soy un trofeo"
    points = 200
    TrophyRepository.add_trophy(Trophy(customId=customId, description=description, points=points))
    result = TrophyRepository.get_all_trophies()
    assert len(result) == 1
    assert result[0].customId == customId
    assert result[0].description == description
    assert result[0].points == points


def test_delete_all_trophies(init):
    customId = 1
    description = "soy un trofeo"
    points = 200
    TrophyRepository.add_trophy(Trophy(customId=customId, description=description, points=points))
    TrophyRepository.delete_all_trophies()
    result = TrophyRepository.get_all_trophies()
    assert result.count() == 0

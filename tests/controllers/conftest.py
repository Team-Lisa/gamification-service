import pytest
from api.Repositories.trophy_repository import TrophyRepository
from api.Repositories.db import DataBase


@pytest.fixture
def init():
    DataBase()
    TrophyRepository.delete_all_trophies()
    return 0

import pytest
from api.Repositories.trophy_repository import TrophyRepository
from api.Repositories.db import DataBase
from api.Repositories.user_status_repository import UserStatusRepository


@pytest.fixture
def init():
    DataBase()
    TrophyRepository.delete_all_trophies()
    UserStatusRepository.delete_all_users_status()
    return 0

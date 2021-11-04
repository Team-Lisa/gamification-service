from datetime import datetime

from api.Repositories.user_status_repository import UserStatusRepository
from api.controllers.constants import *
from api.models.user_status import UserStatus


def test_add_user_status_successfully(init):
    email = "email@email.com"
    actual_time = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    user_status = UserStatus(email=email, lives=LIVES, last_life_actualization=actual_time,
                             actual_time=actual_time, trophies=TROPHIES, history=HISTORY, extra_minutes=EXTRA_MINUTES,
                             fast_forward_exam=FAST_FORWARD_EXAM, points=POINTS)
    result = UserStatusRepository.add_user_status(user_status)
    assert result["id"] != None
    assert result.email == email
    assert result.lives == LIVES
    assert result.trophies == TROPHIES
    assert result.history == HISTORY
    assert result.extra_minutes == EXTRA_MINUTES
    assert result.fast_forward_exam == FAST_FORWARD_EXAM
    assert result.points == POINTS
    assert result.last_life_actualization != None
    assert result.actual_time != None


def test_get_user_status_successfully(init):
    email = "email@email.com"
    actual_time = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    user_status = UserStatus(email=email, lives=LIVES, last_life_actualization=actual_time,
                             actual_time=actual_time, trophies=TROPHIES, history=HISTORY, extra_minutes=EXTRA_MINUTES,
                             fast_forward_exam=FAST_FORWARD_EXAM, points=POINTS)
    UserStatusRepository.add_user_status(user_status)
    result = UserStatusRepository.get_user_status_by_email(email)[0]
    assert result.email == email
    assert result.lives == LIVES
    assert result.trophies == TROPHIES
    assert result.history == HISTORY
    assert result.extra_minutes == EXTRA_MINUTES
    assert result.fast_forward_exam == FAST_FORWARD_EXAM
    assert result.points == POINTS
    assert result.last_life_actualization != None
    assert result.actual_time != None
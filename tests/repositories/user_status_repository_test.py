from datetime import datetime

from api.Repositories.user_status_repository import UserStatusRepository
from api.controllers.constants import *
from api.models.user_status import UserStatus


def test_add_user_status_successfully(init):
    email = "email@email.com"
    actual_time = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    user_status = UserStatus(email=email, lives=LIVES, last_life_actualization=actual_time,
                             trophies=TROPHIES, history=HISTORY, extra_minutes=EXTRA_MINUTES,
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


def test_get_user_status_successfully(init):
    email = "email@email.com"
    actual_time = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    user_status = UserStatus(email=email, lives=LIVES, last_life_actualization=actual_time,
                             trophies=TROPHIES, history=HISTORY, extra_minutes=EXTRA_MINUTES,
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

def test_update_user_lives(init):
    email = "email@email.com"
    new_lives = 3
    actual_time = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    user_status = UserStatus(email=email, lives=LIVES, last_life_actualization=actual_time,
                             trophies=TROPHIES, history=HISTORY, extra_minutes=EXTRA_MINUTES,
                             fast_forward_exam=FAST_FORWARD_EXAM, points=POINTS)
    UserStatusRepository.add_user_status(user_status)
    response = UserStatusRepository.update_user_lives(email, new_lives)
    assert response[0]["lives"] == LIVES + new_lives
    assert response[0]["email"] == email
    assert response[0]["trophies"] == TROPHIES
    assert response[0]["history"] == HISTORY
    assert response[0]["extra_minutes"] == EXTRA_MINUTES
    assert response[0]["fast_forward_exam"] == FAST_FORWARD_EXAM
    assert response[0]["points"] == POINTS
    assert response[0]["last_life_actualization"] != None

def test_update_user_points(init):
    email = "email@email.com"
    new_points = 3
    actual_time = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    user_status = UserStatus(email=email, lives=LIVES, last_life_actualization=actual_time,
                             trophies=TROPHIES, history=HISTORY, extra_minutes=EXTRA_MINUTES,
                             fast_forward_exam=FAST_FORWARD_EXAM, points=POINTS)
    UserStatusRepository.add_user_status(user_status)
    response = UserStatusRepository.update_user_points(email, new_points)
    assert response[0]["points"] == POINTS + new_points
    assert response[0]["lives"] == LIVES
    assert response[0]["email"] == email
    assert response[0]["trophies"] == TROPHIES
    assert response[0]["history"] == HISTORY
    assert response[0]["extra_minutes"] == EXTRA_MINUTES
    assert response[0]["fast_forward_exam"] == FAST_FORWARD_EXAM
    assert response[0]["last_life_actualization"] != None


def test_update_user_minutes(init):
    email = "email@email.com"
    new_minutes = 3
    actual_time = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    user_status = UserStatus(email=email, lives=LIVES, last_life_actualization=actual_time,
                             trophies=TROPHIES, history=HISTORY, extra_minutes=EXTRA_MINUTES,
                             fast_forward_exam=FAST_FORWARD_EXAM, points=POINTS)
    UserStatusRepository.add_user_status(user_status)
    response = UserStatusRepository.update_user_minutes(email, new_minutes)
    assert response[0]["extra_minutes"] == EXTRA_MINUTES + new_minutes
    assert response[0]["points"] == POINTS
    assert response[0]["lives"] == LIVES
    assert response[0]["email"] == email
    assert response[0]["trophies"] == TROPHIES
    assert response[0]["history"] == HISTORY
    assert response[0]["fast_forward_exam"] == FAST_FORWARD_EXAM
    assert response[0]["last_life_actualization"] != None

def test_update_user_fastforwards(init):
    email = "email@email.com"
    amount = 3
    actual_time = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    user_status = UserStatus(email=email, lives=LIVES, last_life_actualization=actual_time,
                             trophies=TROPHIES, history=HISTORY, extra_minutes=EXTRA_MINUTES,
                             fast_forward_exam=FAST_FORWARD_EXAM, points=POINTS)
    UserStatusRepository.add_user_status(user_status)
    response = UserStatusRepository.update_user_fastforwards(email, amount)
    assert response[0]["fast_forward_exam"] == FAST_FORWARD_EXAM + amount
    assert response[0]["extra_minutes"] == EXTRA_MINUTES
    assert response[0]["points"] == POINTS
    assert response[0]["lives"] == LIVES
    assert response[0]["email"] == email
    assert response[0]["trophies"] == TROPHIES
    assert response[0]["history"] == HISTORY
    assert response[0]["last_life_actualization"] != None
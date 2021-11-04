import pytest
from api.controllers.constants import *
from api.controllers.gamification_controller import GamificationController
from api.models.requests.lives import Lives
from api.models.requests.trophies import Trophy
from fastapi import HTTPException

from api.models.requests.user import User


def test_create_trophy_sucessfully(init):
    description = "soy un trofeo"
    points = 200
    trophy = Trophy(description=description,points=points)
    response = GamificationController.create(trophy)
    assert response["trophy"]["id"] != None
    assert response == {
        "trophy": {
            "id": response["trophy"]["id"],
            "description": description,
            "points": points

        }
    }

def test_get_all_trophies_sucessfully(init):
    description = "soy un trofeo"
    points = 200
    trophy = Trophy(description=description,points=points)
    GamificationController.create(trophy)
    response = GamificationController.get_trophies()
    assert response == {
        "trophies": [{
            "id": response["trophies"][0]["id"],
            "description": description,
            "points": points

        }]
    }

def test_create_user_status(init):
    user = User(email = "email@email.com")
    response = GamificationController.create_user_status(user)
    assert response["user_status"]["email"] == user.email
    assert response["user_status"]["lives"] == LIVES
    assert response["user_status"]["trophies"] == TROPHIES
    assert response["user_status"]["history"] == HISTORY
    assert response["user_status"]["extra_minutes"] == EXTRA_MINUTES
    assert response["user_status"]["fast_forward_exam"] == FAST_FORWARD_EXAM
    assert response["user_status"]["points"] == POINTS
    assert response["user_status"]["last_life_actualization"] != None
    assert response["user_status"]["actual_time"] != None

def test_get_user_status(init):
    user = User(email = "email@email.com")
    GamificationController.create_user_status(user)
    response = GamificationController.get_user_status_by_email(user.email)
    assert response["user_status"]["email"] == user.email
    assert response["user_status"]["lives"] == LIVES
    assert response["user_status"]["trophies"] == TROPHIES
    assert response["user_status"]["history"] == HISTORY
    assert response["user_status"]["extra_minutes"] == EXTRA_MINUTES
    assert response["user_status"]["fast_forward_exam"] == FAST_FORWARD_EXAM
    assert response["user_status"]["points"] == POINTS
    assert response["user_status"]["last_life_actualization"] != None
    assert response["user_status"]["actual_time"] != None


def test_get_user_lives_by_email(init):
    user = User(email = "email@email.com")
    GamificationController.create_user_status(user)
    response = GamificationController.get_user_lives_by_email(user.email)
    assert response["lives"] == LIVES
    assert response["last_life_actualization"] != None
    assert response["actual_time"] != None

def test_update_user_lives_by_email(init):
    user = User(email = "email@email.com")
    lives = Lives(lives=1)
    GamificationController.create_user_status(user)
    response = GamificationController.update_user_lives(user.email,lives)
    assert response["lives"] == LIVES + lives.lives
    assert response["last_life_actualization"] != None
    assert response["actual_time"] != None

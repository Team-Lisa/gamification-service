import pytest

from api.controllers.gamification_controller import GamificationController
from api.models.requests.trophies import Trophy
from fastapi import HTTPException


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
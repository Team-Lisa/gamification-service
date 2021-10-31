import pytest

from api.controllers.gamification_controller import GamificationController
from api.models.requests.trophies import Trophy
from fastapi import HTTPException


def test_response(init):
    customId = 1
    description = "soy un trofeo"
    points = 200
    trophy = Trophy(customId=customId,description=description,points=points)
    response = GamificationController.create(trophy)
    assert response == {
        "trophy": {
            "customId": customId,
            "description": description,
            "points": points

        }
    }


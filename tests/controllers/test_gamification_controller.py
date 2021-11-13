from api.controllers.constants import *
from api.controllers.gamification_controller import GamificationController
from api.models.requests.fastforwards import Fastforwards
from api.models.requests.lives import Lives
from api.models.requests.minutes import Minutes
from api.models.requests.points import Points
from api.models.requests.trophies import Trophy


from api.models.requests.unit import Unit
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
    assert response["actual_time"] != None


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

def test_get_user_points_by_email(init):
    user = User(email = "email@email.com")
    GamificationController.create_user_status(user)
    response = GamificationController.get_user_points_by_email(user.email)
    assert response == { "points": POINTS }

def test_update_user_points_by_email(init):
    user = User(email = "email@email.com")
    points = Points(points=1)
    GamificationController.create_user_status(user)
    response = GamificationController.update_user_points(user.email,points)
    assert response == { "points": POINTS + points.points}

def test_get_user_minutes_by_email(init):
    user = User(email = "email@email.com")
    GamificationController.create_user_status(user)
    response = GamificationController.get_user_minutes_by_email(user.email)
    assert response == { "extra_minutes": EXTRA_MINUTES }

def test_update_user_minutes_by_email(init):
    user = User(email = "email@email.com")
    minutes = Minutes(extra_minutes=1)
    GamificationController.create_user_status(user)
    response = GamificationController.update_user_minutes(user.email,minutes)
    assert response == { "extra_minutes": EXTRA_MINUTES + minutes.extra_minutes}

def test_get_user_fastforwards_by_email(init):
    user = User(email = "email@email.com")
    GamificationController.create_user_status(user)
    response = GamificationController.get_user_fastforwards_by_email(user.email)
    assert response == { "fastforwards": FAST_FORWARD_EXAM }

def test_update_user_fastforwards_by_email(init):
    user = User(email = "email@email.com")
    fastforwards = Fastforwards(fastforwards=1)
    GamificationController.create_user_status(user)
    response = GamificationController.update_user_fastforwards(user.email,fastforwards)
    assert response == { "fastforwards": FAST_FORWARD_EXAM + fastforwards.fastforwards}


def test_get_certain_unit_of_a_certain_challenge(init):
    user = User(email="email@email.com")
    GamificationController.create_user_status(user)
    unit = Unit(lesonIdCompleted = 1)
    challengeid = "c1"
    unitid = "u1"
    GamificationController.update_unit_info(unit,challengeid,unitid, user.email)
    response = GamificationController.get_certain_unit_of_a_certain_challenge(challengeid,unitid, user.email)
    assert response == {
        "unit": {
            EXAMCOMPLETED: False,
            LESSONSCOMPLETED: ["1"],
            UNITCOMPLETED: False
            }
    }

def test_update_unit_info_update_lesson_completed(init):
    email="email@email.com"
    user = User(email = email)
    GamificationController.create_user_status(user)
    unit = Unit(lesonIdCompleted=1)
    response = GamificationController.update_unit_info(unit,CHALLENGEID1, UNIT1, user.email)
    updated_user = GamificationController.get_user_status_by_email(email)
    assert updated_user["user_status"]["history"][CHALLENGEID1][UNITS][UNIT1][LESSONSCOMPLETED] == ["1"]

def test_update_unit_info_update_exam_completed(init):
    email="email@email.com"
    user = User(email = email)
    GamificationController.create_user_status(user)
    unit = Unit(examCompleted=True)
    response = GamificationController.update_unit_info(unit,CHALLENGEID1, UNIT1, user.email)
    updated_user = GamificationController.get_user_status_by_email(email)
    assert updated_user["user_status"]["history"][CHALLENGEID1][UNITS][UNIT1][EXAMCOMPLETED] == True

def test_update_unit_info_update_unit_completed(init):
    email="email@email.com"
    user = User(email = email)
    GamificationController.create_user_status(user)
    unit = Unit(unitCompleted=True)
    GamificationController.update_unit_info(unit,CHALLENGEID1, UNIT1, user.email)
    updated_user = GamificationController.get_user_status_by_email(email)
    assert updated_user["user_status"]["history"][CHALLENGEID1][UNITS][UNIT1][UNITCOMPLETED] == True

def test_update_all_unit_info(init):
    email="email@email.com"
    user = User(email = email)
    GamificationController.create_user_status(user)
    unit = Unit(unitCompleted=True,examCompleted=True,lesonIdCompleted=1)
    GamificationController.update_unit_info(unit,CHALLENGEID1, UNIT1, user.email)
    updated_user = GamificationController.get_user_status_by_email(email)
    assert updated_user["user_status"]["history"][CHALLENGEID1][UNITS][UNIT1][UNITCOMPLETED] == True
    assert updated_user["user_status"]["history"][CHALLENGEID1][UNITS][UNIT1][EXAMCOMPLETED] == True
    assert updated_user["user_status"]["history"][CHALLENGEID1][UNITS][UNIT1][LESSONSCOMPLETED] == ["1"]

def test_update_challnge_completed(init):
    email = "email@email.com"
    user = User(email=email)
    GamificationController.create_user_status(user)
    unit = Unit(lesonIdCompleted=1)
    challengeid = "c1"
    unitid = "u1"
    GamificationController.update_unit_info(unit, challengeid, unitid, user.email)
    GamificationController.update_challenge_completed(challengeid,email)
    updated_user = GamificationController.get_user_status_by_email(email)
    assert updated_user["user_status"]["history"][challengeid][CHALLENGECOMPLETED] == True

def test_update_throphie_completed(init):
    email = "email@email.com"
    throphieID = "1"
    user = User(email=email)
    GamificationController.create_user_status(user)
    GamificationController.update_throphy_completed(throphieID,email)
    updated_user = GamificationController.get_user_status_by_email(email)
    assert updated_user["user_status"]["trophies"] == [throphieID]

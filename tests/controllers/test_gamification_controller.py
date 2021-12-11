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
    rules = {"count": 1}
    trophy = Trophy(description=description,points=points, rules = rules)
    response = GamificationController.create(trophy)
    assert response["trophy"]["id"] != None
    assert response == {
        "trophy": {
            "id": response["trophy"]["id"],
            "description": description,
            "points": points,
            "rules": rules
        }
    }

def test_get_all_trophies_sucessfully(init):
    description = "soy un trofeo"
    points = 200
    rules = {"count": 1}
    trophy = Trophy(description=description,points=points, rules=rules)
    GamificationController.create(trophy)
    response = GamificationController.get_trophies()
    assert response == {
        "trophies": [{
            "id": response["trophies"][0]["id"],
            "description": description,
            "points": points,
            "rules":rules

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
    lives = Lives(lives=-1)
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
    assert response == {'won_trophies': []}
    user_status = GamificationController.get_user_status_by_email(user.email)
    assert user_status["user_status"]["extra_minutes"] == EXTRA_MINUTES + minutes.extra_minutes

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
    assert response == {'won_trophies': []}
    user_status = GamificationController.get_user_status_by_email(user.email)
    assert user_status["user_status"]["fast_forward_exam"] == FAST_FORWARD_EXAM + fastforwards.fastforwards


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
"""
def test_update_unit_info_update_unit_completed(init):
    email="email@email.com"
    user = User(email = email)
    GamificationController.create_user_status(user)
    unit = Unit(unitCompleted=True)
    with requests_mock.Mocker() as m:
        json = {"challenge": {"units":[]}}
        m.register_uri('GET', url, json=json, status_code=200)
        response = Exercises.get_challenges()

        assert response == json
    GamificationController.update_unit_info(unit,CHALLENGEID1, UNIT1, user.email)
    updated_user = GamificationController.get_user_status_by_email(email)

    assert updated_user["user_status"]["history"][CHALLENGEID1][UNITS][UNIT1][UNITCOMPLETED] == True
"""

""" 
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

"""

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

def test_get_a_trophy_for_completing_one_lesson(init):
    email = "email@email.com"
    user = User(email=email)
    GamificationController.create_user_status(user)
    description = "completar 1 leccion"
    points = 200
    rules =  {COUNTLESSONS : 1}
    trophy = Trophy(description=description, points=points, rules=rules)
    result_trophy = GamificationController.create(trophy)
    unit = Unit(lesonIdCompleted = "l1")
    challenge_id = "c1"
    unit_id = "u1"
    result = GamificationController.update_unit_info(unit,challenge_id,unit_id,email)
    user_status = GamificationController.get_user_status_by_email(email)
    assert user_status["user_status"]["trophies"] == [result_trophy["trophy"]["id"]]
    assert user_status["user_status"]["points"] == points
    assert result == {"won_trophies": [result_trophy["trophy"]["id"]]}

def test_get_a_trophy_for_completing_5_lessons(init):
    email = "email@email.com"
    user = User(email=email)
    GamificationController.create_user_status(user)
    description = "completar 1 leccion"
    points_1 = 200
    rules = {COUNTLESSONS: 1}
    trophy = Trophy(description=description, points=points_1, rules=rules)
    result_trophy_1 = GamificationController.create(trophy)
    description = "completar 5 lecciones"
    points_2 = 200
    rules = {COUNTLESSONS: 5}
    trophy = Trophy(description=description, points=points_2, rules=rules)
    result_trophy_2 = GamificationController.create(trophy)
    for i in range(5):
        unit = Unit(lesonIdCompleted="{}".format(i))
        challenge_id = "c1"
        unit_id = "u1"
        result = GamificationController.update_unit_info(unit, challenge_id, unit_id, email)
    user_status = GamificationController.get_user_status_by_email(email)
    assert user_status["user_status"]["trophies"] == [result_trophy_1["trophy"]["id"],result_trophy_2["trophy"]["id"]]
    assert user_status["user_status"]["points"] == points_1 + points_2
    assert result == {"won_trophies": [result_trophy_2["trophy"]["id"]]}

"""
def test_get_a_trophy_for_completing_1_unit(init):
    email = "email@email.com"
    user = User(email=email)
    GamificationController.create_user_status(user)
    description = "completar 1 unidad"
    points = 200
    rules = {COUNTUNITS: 1}
    trophy = Trophy(description=description, points=points, rules=rules)
    result_trophy = GamificationController.create(trophy)
    unit = Unit(unitCompleted = True)
    challenge_id = "c1"
    unit_id = "u1"
    result = GamificationController.update_unit_info(unit, challenge_id, unit_id, email)
    user_status = GamificationController.get_user_status_by_email(email)
    assert user_status["user_status"]["trophies"] == [result_trophy["trophy"]["id"]]
    assert user_status["user_status"]["points"] == points
    assert result == {"won_trophies": [result_trophy["trophy"]["id"]]}

"""

def test_get_a_trophy_for_completing_1_challenge(init):
    email = "email@email.com"
    user = User(email=email)
    GamificationController.create_user_status(user)
    description = "completar 1 desafio"
    points = 200
    rules = {COUNTCHALLENGES: 1}
    trophy = Trophy(description=description, points=points, rules=rules)
    result_trophy = GamificationController.create(trophy)
    unit = Unit()
    challenge_id = "c1"
    unit_id = "u1"
    GamificationController.update_unit_info(unit, challenge_id, unit_id, email)
    result = GamificationController.update_challenge_completed(challenge_id,email)
    user_status = GamificationController.get_user_status_by_email(email)
    assert user_status["user_status"]["trophies"] == [result_trophy["trophy"]["id"]]
    assert user_status["user_status"]["points"] == points
    assert result == {"won_trophies": [result_trophy["trophy"]["id"]]}

def test_get_a_trophy_for_buying_one_minute_from_store(init):
    email = "email@email.com"
    user = User(email=email)
    GamificationController.create_user_status(user)
    description = "comprar algo de la tienda"
    points = 200
    rules =  {COUNTBUYEDITEMS : 1}
    trophy = Trophy(description=description, points=points, rules=rules)
    result_trophy = GamificationController.create(trophy)
    minutes = Minutes(extra_minutes = 1)
    result = GamificationController.update_user_minutes(email, minutes)
    user_status = GamificationController.get_user_status_by_email(email)
    assert user_status["user_status"]["trophies"] == [result_trophy["trophy"]["id"]]
    assert user_status["user_status"]["points"] == points
    assert result == {"won_trophies": [result_trophy["trophy"]["id"]]}

def test_get_a_trophy_for_buying_one_fastforward_from_store(init):
    email = "email@email.com"
    user = User(email=email)
    GamificationController.create_user_status(user)
    description = "comprar algo de la tienda"
    points = 200
    rules =  {COUNTBUYEDITEMS : 1}
    trophy = Trophy(description=description, points=points, rules=rules)
    result_trophy = GamificationController.create(trophy)
    fastforward = Fastforwards(fastforwards = 1)
    result = GamificationController.update_user_fastforwards(email, fastforward)
    user_status = GamificationController.get_user_status_by_email(email)
    assert user_status["user_status"]["trophies"] == [result_trophy["trophy"]["id"]]
    assert user_status["user_status"]["points"] == points
    assert result == {"won_trophies": [result_trophy["trophy"]["id"]]}

def test_get_a_trophy_for_buying_one_life_from_store(init):
    email = "email@email.com"
    user = User(email=email)
    GamificationController.create_user_status(user)
    description = "comprar algo de la tienda"
    points = 200
    rules =  {COUNTBUYEDITEMS : 1}
    trophy = Trophy(description=description, points=points, rules=rules)
    result_trophy = GamificationController.create(trophy)
    lives = Lives(lives = 1, market = True)
    result = GamificationController.update_user_lives(email, lives)
    user_status = GamificationController.get_user_status_by_email(email)
    assert user_status["user_status"]["trophies"] == [result_trophy["trophy"]["id"]]
    assert user_status["user_status"]["points"] == points
    assert result["won_trophies"] == [result_trophy["trophy"]["id"]]

def test_get_a_trophy_for_doing_every_exercise_from_exam_correctly(init):
    email = "email@email.com"
    user = User(email=email)
    GamificationController.create_user_status(user)
    description = "hacer todos los ejercicios bien en un examen"
    points = 200
    rules =  {ALLEXERCISESEXAM : True}
    trophy = Trophy(description=description, points=points, rules=rules)
    result_trophy = GamificationController.create(trophy)
    unit = Unit(allExercisesExam=True)
    challenge_id = "c1"
    unit_id = "u1"
    result = GamificationController.update_unit_info(unit, challenge_id, unit_id, email)
    user_status = GamificationController.get_user_status_by_email(email)
    assert user_status["user_status"]["trophies"] == [result_trophy["trophy"]["id"]]
    assert user_status["user_status"]["points"] == points
    assert result["won_trophies"] == [result_trophy["trophy"]["id"]]

def test_get_a_trophy_for_doing_an_exam_in_less_than_5_minutes(init):
    email = "email@email.com"
    user = User(email=email)
    GamificationController.create_user_status(user)
    description = "completar examen en menos de 5 minutos"
    points = 200
    rules =  {TIME : 1}
    trophy = Trophy(description=description, points=points, rules=rules)
    result_trophy = GamificationController.create(trophy)
    unit = Unit(time=True)
    challenge_id = "c1"
    unit_id = "u1"
    result = GamificationController.update_unit_info(unit, challenge_id, unit_id, email)
    user_status = GamificationController.get_user_status_by_email(email)
    assert user_status["user_status"]["trophies"] == [result_trophy["trophy"]["id"]]
    assert user_status["user_status"]["points"] == points
    assert result["won_trophies"] == [result_trophy["trophy"]["id"]]

def test_get_a_trophy_for_doing_every_exercise_from_a_lesson_correctly(init):
    email = "email@email.com"
    user = User(email=email)
    GamificationController.create_user_status(user)
    description = "hacer todos los ejercicios bien en una leccion"
    points = 200
    rules =  {ALLEXERCISESLESSON : True}
    trophy = Trophy(description=description, points=points, rules=rules)
    result_trophy = GamificationController.create(trophy)
    unit = Unit(allExercisesLesson=True)
    challenge_id = "c1"
    unit_id = "u1"
    result = GamificationController.update_unit_info(unit, challenge_id, unit_id, email)
    user_status = GamificationController.get_user_status_by_email(email)
    assert user_status["user_status"]["trophies"] == [result_trophy["trophy"]["id"]]
    assert user_status["user_status"]["points"] == points
    assert result["won_trophies"] == [result_trophy["trophy"]["id"]]


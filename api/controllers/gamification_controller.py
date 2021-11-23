from api.Repositories.store_items_repository import StoreItemsRepository
from api.Repositories.trophy_repository import TrophyRepository
from api.controllers.constants import *
from datetime import datetime
from api.Repositories.user_status_repository import UserStatusRepository
from api.models.requests.points import Points
from api.models.user_status import UserStatus
from api.models.trophy import Trophy


class GamificationController:

    @staticmethod
    def get_trophies():
        result = TrophyRepository.get_all_trophies()
        result = map(lambda trophy: trophy.convert_to_json_with_id(), list(result))
        return {"trophies": list(result)}

    @staticmethod
    def create(trophy):
        trophy = Trophy(description=trophy.description, points=trophy.points, rules = trophy.rules)
        result = TrophyRepository.add_trophy(trophy)
        return {"trophy": result.convert_to_json_with_id()}

    @staticmethod
    def create_user_status(user):
        time = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
        user_status = UserStatus(email=user.email, lives=LIVES, last_life_actualization=time, trophies=TROPHIES,
                                 history=HISTORY, extra_minutes=EXTRA_MINUTES, fast_forward_exam=FAST_FORWARD_EXAM,
                                 points=POINTS,rules=RULES)
        result = UserStatusRepository.add_user_status(user_status)
        return {"user_status": result.convert_to_json(),
                "actual_time": time
        }

    @staticmethod
    def get_user_status_by_email(email):
        result = UserStatusRepository.get_user_status_by_email(email)
        actual_time = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
        return {
            "user_status": result[0].convert_to_json(),
            "actual_time": actual_time
        }

    @staticmethod
    def get_user_lives_by_email(email):
        result = UserStatusRepository.get_user_status_by_email(email)
        actual_time = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
        return {
            "lives": result[0]["lives"],
            "last_life_actualization": result[0]["last_life_actualization"],
            "actual_time": actual_time
        }

    @staticmethod
    def update_user_lives(email, lives):
        actual_lives = GamificationController.get_user_lives_by_email(email)
        total = actual_lives["lives"] + lives.lives
        if total > 5:
            new_lives = 5
        elif total < 0:
            new_lives = 0
        else:
            new_lives = total
        if actual_lives["lives"] == 5 or lives.lives > 0:
            result = UserStatusRepository.update_user_lives_and_last_life_actualization(email, new_lives)
            if lives.market:
                UserStatusRepository.updateRule(COUNTBUYEDITEMS, email)
                won_trophies = GamificationController.check_if_trophy_has_been_earned(email)
                user_status = GamificationController.get_user_status_by_email(email)
                user_status["user_status"]["trophies"] += won_trophies
                UserStatusRepository.update_trophies(email, user_status["user_status"]["trophies"])
            else:
                won_trophies = []
        else:
            result = UserStatusRepository.update_user_lives(email, new_lives)
        actual_time = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
        return {
            "lives": result[0]["lives"],
            "last_life_actualization": result[0]["last_life_actualization"],
            "actual_time": actual_time,
            "won_trophies": won_trophies
        }

    @staticmethod
    def get_user_points_by_email(email):
        result = UserStatusRepository.get_user_status_by_email(email)
        return {
            "points": result[0]["points"]
        }

    @staticmethod
    def update_user_points(email, points):
        actual_points = GamificationController.get_user_status_by_email(email)
        total = actual_points["user_status"]["points"] + points.points
        new_points = total if total >= 0 else 0
        result = UserStatusRepository.update_user_points(email, new_points)
        return {
            "points": result[0]["points"]
        }

    @staticmethod
    def get_user_minutes_by_email(email):
        result = UserStatusRepository.get_user_status_by_email(email)
        return {
            "extra_minutes": result[0]["extra_minutes"]
        }

    @staticmethod
    def update_user_minutes(email, minutes):
        user_status = GamificationController.get_user_status_by_email(email)
        total = user_status["user_status"]["extra_minutes"] + minutes.extra_minutes
        new_minutes = total if total >= 0 else 0
        UserStatusRepository.update_user_minutes(email, new_minutes)
        if minutes.extra_minutes > 0:
            UserStatusRepository.updateRule(COUNTBUYEDITEMS, email)
            won_trophies = GamificationController.check_if_trophy_has_been_earned(email)
            user_status["user_status"]["trophies"] += won_trophies
            UserStatusRepository.update_trophies(email, user_status["user_status"]["trophies"])
        else:
            won_trophies = []
        return {
            "won_trophies": won_trophies
        }

    @staticmethod
    def get_user_fastforwards_by_email(email):
        result = UserStatusRepository.get_user_status_by_email(email)
        return {
            "fastforwards": result[0]["fast_forward_exam"]
        }

    @staticmethod
    def update_user_fastforwards(email, amount):
        user_status = GamificationController.get_user_status_by_email(email)
        total = user_status["user_status"]["fast_forward_exam"] + amount.fastforwards
        new_amount = total if total >= 0 else 0
        UserStatusRepository.update_user_fastforwards(email, new_amount)
        if amount.fastforwards > 0:
            UserStatusRepository.updateRule(COUNTBUYEDITEMS, email)
            won_trophies = GamificationController.check_if_trophy_has_been_earned(email)
            user_status["user_status"]["trophies"] += won_trophies
            UserStatusRepository.update_trophies(email, user_status["user_status"]["trophies"])
        else:
            won_trophies = []
        return {
            "won_trophies": won_trophies
        }

    @staticmethod
    def get_store_items():
        result = StoreItemsRepository.get_all_items()
        result = map(lambda item: item.convert_to_json_with_id(), list(result))
        return {"items": list(result)}

    @staticmethod
    def get_units_of_a_challenge(challenge_id, email):
        user_status = GamificationController.get_user_status_by_email(email)
        return {"units":
                    user_status["user_status"]["history"][challenge_id][UNITS]
                }

    @staticmethod
    def get_certain_unit_of_a_certain_challenge(challenge_id, unit_id, email):
        user_status = GamificationController.get_user_status_by_email(email)
        return {"unit":
                    user_status["user_status"]["history"][challenge_id][UNITS][unit_id]
                }

    @staticmethod
    def update_unit_info(unit, challenge_id, unit_id, email):
        user_status = GamificationController.get_user_status_by_email(email)["user_status"]
        history = user_status["history"]
        if not challenge_id in history:
            history[challenge_id] = {UNITS: {unit_id:
                                                 {EXAMCOMPLETED: False,
                                                  LESSONSCOMPLETED: [],
                                                  UNITCOMPLETED: False}},
                                     CHALLENGECOMPLETED: False}
        elif challenge_id in history and not unit_id in history[challenge_id][UNITS]:
            history[challenge_id][UNITS][unit_id] = {EXAMCOMPLETED: False,
                                                     LESSONSCOMPLETED: [],
                                                     UNITCOMPLETED: False}
        unit_data = history[challenge_id][UNITS][unit_id]
        if unit.lesonIdCompleted:
            unit_data[LESSONSCOMPLETED].append(unit.lesonIdCompleted)
            UserStatusRepository.updateRule(COUNTLESSONS,email)
        if unit.examCompleted:
            unit_data[EXAMCOMPLETED] = unit.examCompleted
        if unit.unitCompleted:
            unit_data[UNITCOMPLETED] = unit.unitCompleted
            UserStatusRepository.updateRule(COUNTUNITS,email)
        if unit.allExercisesExam:
            UserStatusRepository.updateRule(ALLEXERCISESEXAM, email)
        if unit.allExercisesLesson:
            UserStatusRepository.updateRule(ALLEXERCISESLESSON, email)
        if unit.time:
            if unit.time < MAX_TIME:
                UserStatusRepository.updateRule(TIME, email)
        history[challenge_id][UNITS][unit_id] = unit_data
        won_trophies = GamificationController.check_if_trophy_has_been_earned(email)
        user_status["trophies"] += won_trophies
        UserStatusRepository.update_history(email, history)
        UserStatusRepository.update_trophies(email, user_status["trophies"])
        return {"won_trophies": won_trophies}

    @staticmethod
    def update_challenge_completed(challenge_id, email):
        user_status =  GamificationController.get_user_status_by_email(email)["user_status"]
        history = user_status["history"]
        history[challenge_id][CHALLENGECOMPLETED] = True
        UserStatusRepository.updateRule(COUNTCHALLENGES, email)
        won_trophies = GamificationController.check_if_trophy_has_been_earned(email)
        user_status["trophies"] += won_trophies
        UserStatusRepository.update_history(email, history)
        UserStatusRepository.update_trophies(email, user_status["trophies"])
        return {"won_trophies": won_trophies}

    @staticmethod
    def update_throphy_completed(trophy_id, email):
        trophies = GamificationController.get_user_status_by_email(email)["user_status"]["trophies"]
        trophies.append(trophy_id)
        return UserStatusRepository.update_trophies(email, trophies)

    @staticmethod
    def check_if_trophy_has_been_earned(email):
        won_trophies = []
        trophies = GamificationController.get_trophies()
        user_status = GamificationController.get_user_status_by_email(email)["user_status"]
        for t in trophies["trophies"]:
            key = list(t["rules"].keys())[0]
            value = list(t["rules"].values())[0]
            if user_status["rules"][key] == value and t["id"] not in user_status["trophies"]:
                won_trophies.append(t["id"])
                GamificationController.update_user_points(email,Points(points = t["points"]))
        return won_trophies

    @staticmethod
    def update_points_for_won_trophies(email, trophies):
        for id in trophies:
            trophy = TrophyRepository.get_trophy_by_id(id)
            GamificationController.update_user_points(email,trophy["points"])





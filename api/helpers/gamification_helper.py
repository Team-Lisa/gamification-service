from api.Repositories.trophy_repository import TrophyRepository
from api.Repositories.user_status_repository import UserStatusRepository
from api.controllers.constants import UNITS, EXAMCOMPLETED, LESSONSCOMPLETED, UNITCOMPLETED, CHALLENGECOMPLETED


class GamificationHelper:
    @staticmethod
    def calculate_new_lives(actual_lives,lives):
        total = actual_lives["lives"] + lives.lives
        if total > 5:
            return 5
        elif total < 0:
            return  0
        else:
            return total

    @staticmethod
    def get_user_status_history(challenge_id,unit_id,user_status):
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
        return history


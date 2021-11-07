from datetime import datetime
from api.models.user_status import UserStatus
from api.controllers.constants import *


def test_model_to_json():
    email = "email@email.com"
    actual_time = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    user_status = UserStatus(email=email, lives=LIVES, last_life_actualization=actual_time,
                             trophies=TROPHIES, history=HISTORY, extra_minutes=EXTRA_MINUTES,
                             fast_forward_exam=FAST_FORWARD_EXAM, points=POINTS)
    assert user_status.convert_to_json() == {
        "email": email,
        "lives": LIVES,
        "last_life_actualization": actual_time,
        "trophies": TROPHIES,
        "history": HISTORY,
        "extra_minutes": EXTRA_MINUTES,
        "fast_forward_exam": FAST_FORWARD_EXAM,
        "points": POINTS
    }

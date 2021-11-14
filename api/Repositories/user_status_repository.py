from datetime import datetime
from api.models.user_status import UserStatus


class UserStatusRepository():

    @staticmethod
    def delete_all_users_status():
        UserStatus.objects().delete()

    @staticmethod
    def add_user_status(userStatus):
        return userStatus.save()

    @staticmethod
    def get_user_status_by_email(email):
        return UserStatus.objects(email=email)

    @staticmethod
    def update_user_lives_and_last_life_actualization(email ,new_lives):
        UserStatus.objects(email=email).update(lives=new_lives,last_life_actualization = datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))
        return UserStatusRepository.get_user_status_by_email(email)

    @staticmethod
    def update_user_lives(email ,new_lives):
        UserStatus.objects(email=email).update(lives=new_lives)
        return UserStatusRepository.get_user_status_by_email(email)

    @staticmethod
    def update_user_points(email, new_points):
        UserStatus.objects(email=email).update(points=new_points)
        return UserStatusRepository.get_user_status_by_email(email)

    @staticmethod
    def update_user_minutes(email, new_minutes):
        UserStatus.objects(email=email).update(extra_minutes=new_minutes)
        return UserStatusRepository.get_user_status_by_email(email)

    @staticmethod
    def update_user_fastforwards(email, new_amount):
        UserStatus.objects(email=email).update(fast_forward_exam=new_amount)
        return UserStatusRepository.get_user_status_by_email(email)

    @staticmethod
    def update_history(email,history):
        UserStatus.objects(email=email).update(history=history)
        return {"message": "history updated"}

    @staticmethod
    def update_trophies(email, trophies):
        UserStatus.objects(email=email).update(trophies=trophies)
        return {"message": "trophies updated"}



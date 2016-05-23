from django.db import models
from django.contrib.auth.models import User


class UserScore(models.Model):
    #user information
    user_obj = models.OneToOneField(User, on_delete=models.CASCADE)
    #User score
    score = models.IntegerField(default=0)

    @staticmethod
    def create_user_score(current_user):
        us = UserScore(user_obj_id=current_user, score=0)
        us.save()
        return us

    @staticmethod
    def change_score(score_value, current_user):
        try:
            current_user = UserScore.objects.get(user_obj_id=current_user)
            current_user.score += score_value
            current_user.save()
        except:
            new_user = UserScore.create_user_score(current_user)
            new_user.score += score_value
            new_user.save()

    @staticmethod
    def user_asked_question(current_user):
        UserScore.change_score(5, current_user)

    @staticmethod
    def user_answer_upvoted(current_user):
        UserScore.change_score(10, current_user)

    @staticmethod
    def user_answer_downvoted(current_user):
        UserScore.change_score(-1, current_user)

    @staticmethod
    def downvote_other_users_answer(other_user):
        UserScore.change_score(-5, other_user)

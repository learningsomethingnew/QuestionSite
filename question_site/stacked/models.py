from django.db import models
from django.contrib.auth.models import User


"""Model that tracks the
questions asked from the user"""
class Question(models.Model):
    # user information
    user_obj = models.ForeignKey(User)
    # question from the user
    question_asked = models.CharField(max_length=255)
    # users explanation of the question
    description = models.TextField(blank=True)
    # language input, user must put a keyword in.
    keyword = models.CharField(blank=False, max_length=255)

    class Meta:
        # display questions from most recent
        ordering = ['id']


"""Model that tracks the
answers with a FK to user"""
class Answer(models.Model):
    # user who is answering
    user_obj = models.ForeignKey(User)
    # the users answer
    response = models.TextField(blank=False)
    # score of answer
    score = models.IntegerField(default=10)
from django.shortcuts import render
from django.views.generic import ListView
from .models import Question
# Create your views here.
from django.http import HttpResponse

class QuestionList(ListView):
    model = Question

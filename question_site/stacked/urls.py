from django.conf.urls import url
from .views import QuestionList

from . import views

app_name = 'stacked'

urlpatterns = [
    url(r'^list/$', QuestionList.as_view()),
]

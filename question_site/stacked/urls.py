from django.conf.urls import url
from .views import QuestionList, question_input_form, detail

from . import views

app_name = 'stacked'

urlpatterns = [
    url(r'^questionform/$', question_input_form),
    url(r'^(?P<question_id>[0-9]+)/$', detail, name='detail_view'),

    url(r'^$', QuestionList.as_view()),
]

from django import forms

from stacked.models import Question

class NewQuestionForm(forms.Form):
    question_asked = forms.CharField(max_length=255)
    description = forms.TextInput()
    keyword = forms.CharField(max_length=255)
from django.forms import ModelForm, Textarea
from django import forms
from django.utils import html

class QuestionForm(forms.Form):
    question_asked = forms.CharField(
        max_length=255,
        label="Question",
        required=True,
    )
    description = forms.CharField(
        required=False,
        label="Description"
    )
    keyword = forms.CharField(
        required=True,
        label="Language"
    )


class AnswerForm(forms.Form):
    response = forms.CharField(label="Answer",
                               widget=forms.Textarea)

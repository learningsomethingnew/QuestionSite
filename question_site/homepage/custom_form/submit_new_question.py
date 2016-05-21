from django import forms

from question_site.stacked.models import Question

class NewQuestionForm(forms.ModelForm):
    class Meta:
        model = Question
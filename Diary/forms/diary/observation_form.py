from django import forms
from Diary.models import *


class Observation_form(forms.ModelForm):
    class Meta:
        model = Observation
        fields = '__all__'

from django import forms
from Diary.models import *


class Climate_form(forms.ModelForm):
    class Meta:
        model = Climate
        fields = '__all__'

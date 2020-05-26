from django import forms
from Diary.models import *


class Direct_labor_Form(forms.ModelForm):
    class Meta:
        model = Direct_labor
        fields = '__all__'

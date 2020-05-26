from django import forms
from Diary.models import *


class Contractor_labor_Form(forms.ModelForm):
    class Meta:
        model = Contractor_labor
        fields = '__all__'

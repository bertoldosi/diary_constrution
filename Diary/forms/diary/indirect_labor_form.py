from django import forms
from Diary.models import *


class Indirect_labor_Form(forms.ModelForm):
    class Meta:
        model = Indirect_labor
        fields = '__all__'

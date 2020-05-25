from django import forms
from Diary.models import *


class ConstructionForm(forms.ModelForm):
    class Meta:
        model = Construction
        fields = '__all__'

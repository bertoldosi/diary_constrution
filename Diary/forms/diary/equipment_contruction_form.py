from django import forms
from Diary.models import *


class Equipment_construction_form(forms.ModelForm):
    class Meta:
        model = Equipment_construction
        fields = '__all__'

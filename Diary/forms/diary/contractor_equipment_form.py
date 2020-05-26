from django import forms
from Diary.models import *


class Contractor_equipment_form(forms.ModelForm):
    class Meta:
        model = Contractor_equipment
        fields = '__all__'

from django import forms
from Diary.models import *


class Total_service_form(forms.ModelForm):
    class Meta:
        model = Total_service
        fields = '__all__'

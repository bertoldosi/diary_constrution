from django import forms
from Diary.models import *


class DiaryForm(forms.ModelForm):
    class Meta:
        model = Diary
        fields = '__all__'

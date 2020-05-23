from django import forms
from ..models import Engineer


class Engineer_form(forms.ModelForm):
    class Meta:
        model = Engineer
        fields = ('user_access', 'engineer_name')

from django import forms
from Diary.models import Engineer


class Engineer_form(forms.ModelForm):
    class Meta:
        model = Engineer
        fields = ('user_access',
                  'engineer_name',
                  'engineer_cnpj',
                  'engineer_contact',
                  'engineer_street',
                  'engineer_number',
                  'engineer_city',
                  'engineer_state',
                  'engineer_cod',
                  )

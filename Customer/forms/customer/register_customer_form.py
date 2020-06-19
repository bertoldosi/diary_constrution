from django import forms
from Diary.models import Customer


class Customer_form(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('user_access',
                  'customer_name',
                  'engineer',
                  'customer_cnpj',
                  'customer_contact',
                  'customer_street',
                  'customer_number',
                  'customer_city',
                  'customer_state',
                  'customer_cod'
                  )
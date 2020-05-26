from django import forms
from Diary.models import Customer


class Customer_form(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('user_access', 'customer_name', 'engineer')

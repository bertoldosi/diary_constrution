from django.contrib.auth.forms import AuthenticationForm
from django import forms
from Diary.models import Access


class Login_form(AuthenticationForm):
    username = forms.EmailField()

    class Meta:
        model = Access
        fields = ['username', 'password']

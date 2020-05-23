from django import forms
from ..models import User_access


class User_form(forms.ModelForm):
    password1 = forms.CharField(label='Senha', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirma senha', widget=forms.PasswordInput)

    class Meta:
        model = User_access
        fields = ('email', 'last_login', )

    # verificar se as duas senha são iguais
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('As senhas informadas não são iguais!')
        return password2

    # inserindo a senha no banco criptografada
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user

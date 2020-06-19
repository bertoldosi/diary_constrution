from django import forms
from Diary.models import Access


class Access_form(forms.ModelForm):
    password1 = forms.CharField(label='Senha', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirma senha', widget=forms.PasswordInput)

    class Meta:
        model = Access
        fields = ('email', 'user_type', 'registration_mode', 'last_login',)

    # verificar se as duas senha são iguais
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('As senhas informadas não são iguais!')
        return password2

    # inserindo a senha no banco criptografada
    def save(self, commit=True):
        access = super().save(commit=False)
        access.set_password(self.cleaned_data['password1'])
        if commit:
            access.save()
        return access

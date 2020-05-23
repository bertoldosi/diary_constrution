from django import forms
from ..models import Company_user


class Register_user_form(forms.ModelForm):
    password1 = forms.CharField(label='Senha', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirma senha', widget=forms.PasswordInput)

    class Meta:
        model = Company_user
        fields = ('company_user_name',
                  'company_user_cnpj',
                  'company_user_email',
                  'company_user_responsible',
                  'company_user_contact',
                  'company_user_address_street',
                  'company_user_address_number',
                  'company_user_address_cod',
                  'company_user_address_city',
                  'company_user_address_state')

    # verificar se as duas senha são iguais
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('As senhas informadas não são iguais!')
        return password2

    # inserindo a senha no banco criptofrada
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set__password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user

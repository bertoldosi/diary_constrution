from django.shortcuts import render, redirect

from Diary.entidades.usuario import Usuario
from Diary.forms.user.register_user_form import Register_user_form
from Diary.services import usuario_service


def Register_User(request):
    if request.method == 'POST':
        formuser = Register_user_form(data=request.POST)

        if formuser.is_valid():
            company_user_name = formuser.cleaned_data['company_user_name']
            company_user_cnpj = formuser.cleaned_data['company_user_cnpj']
            company_user_responsible = formuser.cleaned_data['company_user_responsible']
            company_user_contact = formuser.cleaned_data['company_user_contact']
            company_user_email = formuser.cleaned_data['company_user_email']
            company_user_address_street = formuser.cleaned_data['company_user_address_street']
            company_user_address_number = formuser.cleaned_data['company_user_address_number']
            company_user_address_cod = formuser.cleaned_data['company_user_address_cod']
            company_user_address_city = formuser.cleaned_data['company_user_address_city']
            company_user_address_state = formuser.cleaned_data['company_user_address_state']
            password = formuser.cleaned_data['password1']

            usuario_novo = Usuario(company_user_name=company_user_name,
                                   company_user_cnpj=company_user_cnpj,
                                   company_user_responsible=company_user_responsible,
                                   company_user_contact=company_user_contact,
                                   company_user_email=company_user_email,
                                   company_user_address_street=company_user_address_street,
                                   company_user_address_number=company_user_address_number,
                                   company_user_address_cod=company_user_address_cod,
                                   company_user_address_city=company_user_address_city,
                                   company_user_address_state=company_user_address_state,
                                   password=password)
            usuario_service.cadastrar_usuario(usuario_novo)
            return redirect('login')
        else:
            formuser = Register_user_form()
    return render(request, 'Diary/user/register_user.html', locals())
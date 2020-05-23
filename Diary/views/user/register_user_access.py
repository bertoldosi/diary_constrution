from django.shortcuts import render, redirect

from Diary.entidades.user_access import User
from Diary.forms.register_user_access_form import User_form
from Diary.services import user_service_access


def Register_User(request):
    form_user = User_form()
    if request.method == 'POST':
        form_user = User_form(data=request.POST)
        if form_user.is_valid():
            email = form_user.cleaned_data['email']
            password = form_user.cleaned_data['password1']

            user_new = User(email=email, password=password)

            user_service_access.Register_user(user_new)

            return redirect('login')
    else:
        form_user = User_form()
    return render(request, 'Diary/user/register_user_access.html', locals())
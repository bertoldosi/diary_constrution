from django.shortcuts import render, redirect
from Diary.entidades.user_access import Access
from Diary.forms.user.register_access_form import Access_form
from Diary.services import access_service


def Register_access(request):
    form_access = Access_form()
    if request.method == 'POST':
        form_access = Access_form(data=request.POST)
        if form_access.is_valid():
            email = form_access.cleaned_data['email']
            user_type = form_access.cleaned_data['user_type']
            registration_mode = form_access.cleaned_data['registration_mode']
            password = form_access.cleaned_data['password1']

            access_new = Access(email=email, password=password, user_type=user_type, registration_mode=registration_mode)

            access_service.Register_access(access_new)

            return redirect('login')
    else:
        form_user = Access_form()
    return render(request, 'Diary/user/register_access.html', locals())

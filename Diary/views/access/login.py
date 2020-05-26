from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from Diary.forms.user.login_form import Login_form
from Diary.models import Access


def Login(request):
    usuarios = Access.objects.all()
    form_login = Login_form()
    if request.method == 'POST':
        form_login = Login_form(data=request.POST)

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:

            if user.last_login is None:
                login(request, user)
                if user.user_type == 'Engenheiro':
                    return redirect('register_engineer')
                elif user.user_type == 'Cliente':
                    return redirect('register_customer')
            else:
                login(request, user)
                return redirect('home_page')
        else:
            form_login = Login_form()
    else:
        form_login = Login_form()
    return render(request, 'Diary/access/login.html', locals())
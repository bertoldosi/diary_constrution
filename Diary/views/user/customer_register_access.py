from django.shortcuts import render, redirect
from Diary.entidades.user_access import Access
from Diary.forms.user.register_access_form import Access_form
from Diary.services import access_service
from Diary.models import Access


def get_ultimo():
    user = Access.objects.all()
    list_user = []
    for i in user:
        list_user.append(i)

    return list_user[-1]


def Customer_register_access(request):
    form_access = Access_form()
    if request.method == 'POST':
        form_access = Access_form(data=request.POST)
        if form_access.is_valid():
            email = form_access.cleaned_data['email']
            user_type = form_access.cleaned_data['user_type']
            password = form_access.cleaned_data['password1']

            access_new = Access(email=email, password=password, user_type=user_type)

            access_service.Register_access(access_new)

            user = get_ultimo()
            user = user.id

            return redirect('enginner_register_customer', user)
    else:
        form_user = Access_form()
    return render(request, 'Diary/user/customer_register_access.html', locals())

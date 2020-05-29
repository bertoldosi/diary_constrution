from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from Diary.models import *


@login_required(login_url='login')
def Index(request):
    user = request.user
    user = Access.objects.get(id=user.id)

    engineer = Engineer.objects.get(user_access=user)
    constructions = Construction.objects.filter(construction_company_engineer=engineer)

    if user.user_type == 'Engenheiro':
        nome_campo = 'engineer_name'
        usuario = Engineer.objects.get(user_access__email=user.email)
    elif user.user_type == 'Cliente':
        nome_campo = 'engineer_customer'
        usuario = Customer.objects.get(user_access__email=user.email)
    return render(request, 'Diary/home/index.html', locals())

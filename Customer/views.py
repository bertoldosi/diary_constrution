from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from Diary.models import *


# ERRO AO MOSTRAR AS CONSTRUÇÕES DO CUSTOMERS, DA COMO ELE NÃO EXISTE

@login_required(login_url='login')
def Index(request):
    user = request.user
    user = Access.objects.get(id=user.id)
    customer = Customer.objects.get(user_access_id=user.id)
    construction_user = Construction.objects.filter(construction_company_customer_id=customer.id)

    return render(request, 'Customer/home/index.html', locals())

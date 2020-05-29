from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from Diary.entidades.customer import Customer
from Diary.forms.customer.register_customer_form import Customer_form
from Diary.services import customer_service
from Diary.models import *


@login_required(login_url='login')
def Enginner_register_customer(request, user):
    user = int(user)
    usuario = Access.objects.get(id=user)

    usuario_logado = request.user.id

    enginner = Engineer.objects.get(user_access_id=usuario_logado)

    form_customer = Customer_form()

    if request.method == 'POST':
        form_customer = Customer_form(data=request.POST)
        if form_customer.is_valid():
            user_access = form_customer.cleaned_data['user_access']
            customer_name = form_customer.cleaned_data['customer_name']
            engineer = form_customer.cleaned_data['engineer']

            customer = Customer(user_access=user_access, customer_name=customer_name, engineer=engineer)

            customer_service.Register_customer(customer)

            return redirect('show_customer')
    else:
        form_customer = Customer_form()
    return render(request, 'Diary/engineer/engineer_register_customer.html', locals())

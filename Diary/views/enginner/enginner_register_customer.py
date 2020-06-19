from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from Diary.entidades.customer import Customer
from Customer.forms.customer.register_customer_form import Customer_form
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
            engineer = form_customer.cleaned_data['engineer']
            customer_name = form_customer.cleaned_data['customer_name']
            customer_cnpj = form_customer.cleaned_data['customer_cnpj']
            customer_contact = form_customer.cleaned_data['customer_contact']
            customer_street = form_customer.cleaned_data['customer_street']
            customer_number = form_customer.cleaned_data['customer_number']
            customer_city = form_customer.cleaned_data['customer_city']
            customer_state = form_customer.cleaned_data['customer_state']
            customer_cod = form_customer.cleaned_data['customer_cod']

            customer = Customer(user_access=user_access,
                                engineer=engineer,
                                customer_name=customer_name,
                                customer_cnpj=customer_cnpj,
                                customer_contact=customer_contact,
                                customer_street=customer_street,
                                customer_number=customer_number,
                                customer_city=customer_city,
                                customer_state=customer_state,
                                customer_cod=customer_cod,
                                )

            customer_service.Register_customer(customer)

            return redirect('show_customer')
    else:
        form_customer = Customer_form()
    return render(request, 'Diary/engineer/engineer_register_customer.html', locals())

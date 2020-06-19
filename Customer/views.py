import json
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from Customer.forms.customer.register_customer_form import Customer_form
from Customer.services import customer_service
from Diary.forms.user.register_access_form import Access_form
from Diary.models import *


@login_required(login_url='login')
def Index(request):
    user = request.user
    user = Access.objects.get(id=user.id)
    customer = Customer.objects.get(user_access_id=user.id)

    return render(request, 'Customer/home/index.html', locals())


def autocompleteModel(request):
    if request.is_ajax():
        # pegando o nome digitado no post
        nome_customer = request.GET.get('term', '').capitalize()

        # pegando o objeto cujo nome é o digitado no post e usa o "startswith" para exibir
        customer = Engineer.objects.filter(engineer_name__icontains=nome_customer)

        resultado = []
        for r in customer:
            resultado.append(r.engineer_name)
        data = json.dumps(resultado)
    else:
        data = 'Falhou'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)


@login_required(login_url='login')
def Register_customer(request):
    engineer = Engineer.objects.all()
    form_customer = Customer_form()
    user = request.user.id

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

            customer = Customer(
                user_access=user_access,
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

            return redirect('customer:index')
    else:
        form_customer = Customer_form()
    return render(request, 'Diary/customer/register_customer.html', locals())


@login_required(login_url='login')
def Edit_customer(request, id_customer):
    customer = Customer.objects.get(user_access_id=request.user.id)

    form = Customer_form(request.POST or None, instance=customer)
    if form.is_valid():
        form.save()
        return redirect('customer:profile')
    return render(request, 'Customer/customer/edit_customer.html', locals())


@login_required(login_url='login')
def List_customer(request):
    user = request.user

    customer = Customer.objects.get(user_access_id=user.id)
    return render(request, 'Customer/customer/list_customer.html', locals())


@login_required(login_url='login')
def Change_password(request):
    user = Access.objects.get(id=request.user.id)
    form = Access_form(request.POST or None, instance=user)
    if form.is_valid():
        form.save()
        return redirect('customer:index')
    return render(request, 'Customer/customer/change_password.html', locals())


@login_required(login_url='login')
def Profile(request):
    customer = Customer.objects.get(user_access_id=request.user.id)
    return render(request, 'Customer/home/profile.html', locals())

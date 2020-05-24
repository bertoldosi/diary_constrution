import json
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from Diary.entidades.customer import Customer
from Diary.entidades.engineer import Engineer
from Diary.forms.register_customer_form import Customer_form
from Diary.services import customer_service
from Diary.models import Engineer


def autocompleteModel(request):
    if request.is_ajax():
        #pegando o nome digitado no post
        nome_engineer = request.GET.get('term', '').capitalize()

        #pegando o objeto cujo nome é o digitado no post e usa o "startswith" para exibir
        engineer = Engineer.objects.filter(engineer_name__startswith=nome_engineer)

        resultado = []
        for r in engineer:
            resultado.append(r.engineer_name)
        data = json.dumps(resultado)
    else:
        data = 'Falhou'

    mimetype = 'application/json'
    return HttpResponse(data, mimetype)


@login_required(login_url='login')
def Register_customer(request):
    form_customer = Customer_form()
    user = request.user.id
    if request.method == 'POST':
        form_customer = Customer_form(data=request.POST)
        if form_customer.is_valid():

            user_access = form_customer.cleaned_data['user_access']
            customer_name = form_customer.cleaned_data['customer_name']
            engineer = form_customer.cleaned_data['engineer']

            customer = Customer(user_access=user_access, customer_name=customer_name, engineer=engineer)

            customer_service.Register_customer(customer)

            return redirect('home_page')
    else:
        form_customer = Customer_form()
    return render(request, 'Diary/customer/register_customer.html', locals())

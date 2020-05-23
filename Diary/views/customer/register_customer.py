from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from Diary.entidades.customer import Customer
from Diary.entidades.engineer import Engineer
from Diary.forms.register_customer_form import Customer_form
from Diary.services import customer_service


@login_required(login_url='login')
def Register_customer(request):
    form_customer = Customer_form()
    user = request.user.id
    if request.method == 'POST':
        form_customer = Customer_form(data=request.POST)
        if form_customer.is_valid():

            user_access = form_customer.cleaned_data['user_access']
            customer_name = form_customer.cleaned_data['customer_name']

            customer = Customer(user_access=user_access, customer_name=customer_name)

            customer_service.Register_customer(customer)

            return redirect('home_page')
    else:
        form_customer = Customer_form()
    return render(request, 'Diary/customer/register_customer.html', locals())

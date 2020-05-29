from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from Diary.forms.customer.register_customer_form import Customer_form
from Diary.models import Customer


@login_required(login_url='login')
def Edit_customer(request, id_customer):
    customer = Customer.objects.get(id=id_customer)

    form = Customer_form(request.POST or None, instance=customer)
    if form.is_valid():
        form.save()
        return redirect('show_customer')
    return render(request, 'Diary/customer/edit_customer.html', locals())

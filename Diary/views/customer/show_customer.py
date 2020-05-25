from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from Diary.models import *


@login_required(login_url='login')
def Show_customer(request):
    user = request.user

    engineer = Engineer.objects.get(user_access=user)
    customers = Customer.objects.filter(engineer=engineer)

    return render(request, 'Diary/customer/show_customer.html', locals())

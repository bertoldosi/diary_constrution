from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required(login_url='login')
def Edit_customer(request):
    return render(request, 'Diary/customer/edit_customer.html')
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required(login_url='login')
def Select_customer(request):
    return render(request, 'Diary/construction/select_customer.html')
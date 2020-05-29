from datetime import date
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from Diary.forms.construction.constructionForm import ConstructionForm
from Diary.models import *


@login_required(login_url='login')
def Register_construction(request):
    customers = Customer.objects.all()
    engineer = Engineer.objects.get(user_access_id=request.user.id)
    data = date.today()
    form_construction = ConstructionForm()
    if request.method == 'POST':
        form_construction = ConstructionForm(request.POST)
        if form_construction.is_valid():
            form_construction.save()
            return redirect('show_constructions')
        else:
            HttpResponse('Deu errado!')
    return render(request, 'Diary/construction/register_construction.html', locals())

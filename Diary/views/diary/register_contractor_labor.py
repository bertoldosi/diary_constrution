from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from Diary.forms.diary.contractor_labor_form import Contractor_labor_Form
from Diary.models import *


@login_required(login_url='login')
def Register_contractor_labor(request, diary):
    number_contractor_labor = int(diary)
    contractor_labor = Contractor_labor.objects.filter(contractor_labor_diary_id=number_contractor_labor)
    contractor_labor_form = Contractor_labor_Form()
    if request.method == 'POST':
        contractor_labor_form = Contractor_labor_Form(request.POST)
        if contractor_labor_form.is_valid():
            contractor_labor_form.save()
            return redirect('register_contractor_labor', diary)
        else:
            HttpResponse('Formulário inválido!')
    return render(request, 'Diary/diary/register_contractor_labor.html', locals())

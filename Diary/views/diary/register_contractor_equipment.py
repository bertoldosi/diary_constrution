from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from Diary.forms.diary.contractor_equipment_form import Contractor_equipment_form
from Diary.models import *


@login_required(login_url='login')
def Register_equipment_contractor(request, diary):
    number_contractor_equipment = int(diary)
    contractor_equipment = Contractor_equipment.objects.filter(contractor_equipment_diary_id=number_contractor_equipment)
    contractor_equipment_form = Contractor_equipment_form()
    if request.method == 'POST':
        contractor_equipment_form = Contractor_equipment_form(request.POST)
        if contractor_equipment_form.is_valid():
            contractor_equipment_form.save()
            return redirect('register_equipment_contractor', diary)
        else:
            HttpResponse('Formulário inválido!')
    return render(request, 'Diary/diary/register_equipment_contractor.html', locals())

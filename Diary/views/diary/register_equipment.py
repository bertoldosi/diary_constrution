from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from Diary.forms.diary.equipment_contruction_form import Equipment_construction_form
from Diary.models import *


@login_required(login_url='login')
def Register_equipment(request, diary):
    equipment_construction_form = Equipment_construction_form()
    if request.method == 'POST':
        equipment_construction_form = Equipment_construction_form(request.POST)
        if equipment_construction_form.is_valid():
            equipment_construction_form.save()
            return redirect('register_equipment_contractor', diary)

        else:
            HttpResponse('Formulário inválido!')
    return render(request, 'Diary/diary/register_equipment.html', locals())

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from Diary.forms.diary.contractor_equipment_form import Contractor_equipment_form


@login_required(login_url='login')
def Register_equipment_contractor(request, diary):
    contractor_equipment_form = Contractor_equipment_form()
    if request.method == 'POST':
        contractor_equipment_form = Contractor_equipment_form(request.POST)
        if contractor_equipment_form.is_valid():
            contractor_equipment_form.save()
            return redirect('register_climate', diary)
        else:
            HttpResponse('Formulário inválido!')
    return render(request, 'Diary/diary/register_equipment_contractor.html', locals())

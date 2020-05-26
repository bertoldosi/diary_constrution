from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from Diary.forms.diary.show_total_service_form import Total_service_form
from Diary.models import *


def get_amount_manpower(diary):
    direct_labor = Direct_labor.objects.filter(direct_labor_diary_id=diary)
    indirect_labor = Indirect_labor.objects.filter(indirect_labor_diary_id=diary)
    contractor_labor = Contractor_labor.objects.filter(contractor_labor_diary_id=diary)

    lista01 = []
    for amount in direct_labor:
        qtd = amount.direct_labor_amount
        lista01.append(qtd)
    direct_labor_amount = int(sum(lista01))

    lista02 = []
    for amount in indirect_labor:
        qtd = amount.indirect_labor_amount
        lista02.append(qtd)
    indirect_labor_amount = int(sum(lista01))

    lista03 = []
    for amount in contractor_labor:
        qtd = amount.contractor_labor_amount
        lista03.append(qtd)
    contractor_labor_amount = int(sum(lista01))

    amount_manpower = direct_labor_amount+indirect_labor_amount+contractor_labor_amount

    return amount_manpower


def get_amount_equipment(diary):
    equipment_construction = Equipment_construction.objects.filter(equipment_construction_diary_id=diary)
    contractor_equipment = Contractor_equipment.objects.filter(contractor_equipment_diary_id=diary)

    lista01 = []
    for amount in equipment_construction:
        qtd = amount.equipment_construction_amount
        lista01.append(qtd)
    equipment_construction_amount = int(sum(lista01))

    lista02 = []
    for amount in contractor_equipment:
        qtd = amount.contractor_equipment_amount
        lista02.append(qtd)
    contractor_equipment_amount = int(sum(lista01))

    amount_equipment = equipment_construction_amount + contractor_equipment_amount

    return amount_equipment


@login_required(login_url='login')
def Show_total_service(request, diary):

    amount_manpower = get_amount_manpower(diary)
    amount_equipment = get_amount_equipment(diary)

    show_total_service_form = Total_service_form()
    if request.method == 'POST':
        show_total_service_form = Total_service_form(request.POST)
        if show_total_service_form.is_valid():
            show_total_service_form.save()
            return redirect('register_equipment_contractor', diary)

        else:
            HttpResponse('Formulário inválido!')
    return render(request, 'Diary/diary/show_total_service.html', locals())

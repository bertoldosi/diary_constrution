from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from Diary.models import *


@login_required(login_url='login')
def Show_diary_information(request, id_diary):
    diary = Diary.objects.get(id=id_diary)

    obj_diary = Diary.objects.get(id=id_diary)
    construction = obj_diary.diary_construction_id

    direct_labor = Direct_labor.objects.filter(direct_labor_diary_id=obj_diary.id)
    indirect_labor = Indirect_labor.objects.filter(indirect_labor_diary_id=obj_diary.id)
    contractor_labor = Contractor_labor.objects.filter(contractor_labor_diary_id=obj_diary.id)
    equipment_construction = Equipment_construction.objects.filter(equipment_construction_diary_id=obj_diary.id)
    contractor_equipment = Contractor_equipment.objects.filter(contractor_equipment_diary_id=obj_diary.id)
    climate = Climate.objects.get(climate_diary_id=obj_diary.id)
    total_service = Total_service.objects.get(total_service_diary_id=obj_diary.id)
    observation = Observation.objects.get(observation_diary_id=obj_diary.id)

    return render(request, 'Diary/diary/show_diary_information.html', locals())

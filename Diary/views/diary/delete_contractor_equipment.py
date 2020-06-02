from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from Diary.models import *


@login_required(login_url='login')
def Delete_contractor_equipment(request, diary, equipment_contractor_id):
    equipment_contractor = get_object_or_404(Contractor_equipment, pk=equipment_contractor_id)
    equipment_contractor.delete()
    return redirect('register_equipment_contractor', diary)

from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from Diary.models import *


@login_required(login_url='login')
def Delete_equipment(request, diary, equipment_id):
    equipment = get_object_or_404(Equipment_construction, pk=equipment_id)
    equipment.delete()
    return redirect('register_equipment', diary)

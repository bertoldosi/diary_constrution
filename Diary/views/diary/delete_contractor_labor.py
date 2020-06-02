from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from Diary.models import *


@login_required(login_url='login')
def Delete_contractor_labor(request, diary, contractor_labor_id):
    contractor_labor = get_object_or_404(Contractor_labor, pk=contractor_labor_id)
    contractor_labor.delete()
    return redirect('register_contractor_labor', diary)

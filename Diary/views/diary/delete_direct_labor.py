from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from Diary.models import *


@login_required(login_url='login')
def Delete_direct_labor(request, diary, direct_labor_id):
    direct_labor = get_object_or_404(Direct_labor, pk=direct_labor_id)
    direct_labor.delete()
    return redirect('register_direct_labor', diary)

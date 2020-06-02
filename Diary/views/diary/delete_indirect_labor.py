from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from Diary.models import *


@login_required(login_url='login')
def Delete_indirect_labor(request, diary, indirect_labor_id):
    indirect_labor = get_object_or_404(Indirect_labor, pk=indirect_labor_id)
    indirect_labor.delete()
    return redirect('register_indirect_labor', diary)

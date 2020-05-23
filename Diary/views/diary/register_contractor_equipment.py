from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required(login_url='login')
def Register_equipment_contractor(request):
    return render(request, 'Diary/diary/register_equipment_contractor.html')
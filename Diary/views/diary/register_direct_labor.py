from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required(login_url='login')
def Register_direct_labor(request):
    return render(request, 'Diary/diary/register_direct_labor.html')
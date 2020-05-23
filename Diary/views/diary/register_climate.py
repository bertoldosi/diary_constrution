from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required(login_url='login')
def Register_climate(request):
    return render(request, 'Diary/diary/register_climate.html')
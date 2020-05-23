from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required(login_url='login')
def Show_total_service(request):
    return render(request, 'Diary/diary/show_total_service.html')
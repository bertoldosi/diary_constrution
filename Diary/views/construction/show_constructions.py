from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required(login_url='login')
def Show_constructions(request):
    return render(request, 'Diary/construction/show_constructions.html')
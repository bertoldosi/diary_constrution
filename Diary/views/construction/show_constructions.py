from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from Diary.models import *


@login_required(login_url='login')
def Show_constructions(request):
    user = request.user
    engineer = Engineer.objects.get(user_access_id=user.id)
    constructions = Construction.objects.filter(construction_company_engineer=engineer)
    return render(request, 'Diary/construction/show_constructions.html', locals())

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from Diary.models import *


@login_required(login_url='login')
def Show_construction_information(request, id_construction):
    construction = Construction.objects.get(id=id_construction)
    diary = Diary.objects.filter(diary_construction_id=construction.id)

    return render(request, 'Diary/construction/show_construction_information.html', locals())

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from Diary.models import *


@login_required(login_url='login')
def Show_diary_information(request, id_diary):
    diary = Diary.objects.get(id=id_diary)

    obj_diary = Diary.objects.get(id=id_diary)
    construction = obj_diary.diary_construction_id

    return render(request, 'Diary/diary/show_diary_information.html', locals())

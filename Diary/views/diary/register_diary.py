from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from Diary.forms.diary.diary_form import DiaryForm
from Diary.models import *


def get_ultimo(diarys):
    list_diary = []
    for i in diarys:
        list_diary.append(i)

    return list_diary[-1]


@login_required(login_url='login')
def Register_diary(request, id_construction):
    construction = Construction.objects.get(id=id_construction)

    diarys = Diary.objects.filter(diary_construction_id=construction.id)

    form_diary = DiaryForm()
    if request.method == 'POST':
        form_diary = DiaryForm(request.POST)
        if form_diary.is_valid():
            form_diary.save()

            diary = get_ultimo(diarys)
            diary = diary.id

            return redirect('register_direct_labor', diary)
        else:
            HttpResponse('Formulário inválido')
    return render(request, 'Diary/diary/register_diary.html', locals())

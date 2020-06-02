from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from Diary.forms.diary.direct_labor_form import Direct_labor_Form
from Diary.models import *


@login_required(login_url='login')
def Register_direct_labor(request, diary):
    number_diary = int(diary)
    direct_labor = Direct_labor.objects.filter(direct_labor_diary_id=number_diary)

    direct_labor_form = Direct_labor_Form()
    if request.method == 'POST':
        direct_labor_form = Direct_labor_Form(request.POST)
        if direct_labor_form.is_valid():
            direct_labor_form.save()
            return redirect('register_direct_labor', diary)

        else:
            HttpResponse('Formulário inválido!')
    return render(request, 'Diary/diary/register_direct_labor.html', locals())


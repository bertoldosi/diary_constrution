from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from Diary.forms.diary.indirect_labor_form import Indirect_labor_Form
from Diary.models import *


@login_required(login_url='login')
def Register_indirect_labor(request, diary):
    number_diary = int(diary)
    indirect_labor = Indirect_labor.objects.filter(indirect_labor_diary_id=number_diary)
    indirect_labor_form = Indirect_labor_Form()
    if request.method == 'POST':
        indirect_labor_form = Indirect_labor_Form(request.POST)
        if indirect_labor_form.is_valid():
            indirect_labor_form.save()
            return redirect('register_indirect_labor', diary)
        else:
            HttpResponse('Formulário inválido!')
    return render(request, 'Diary/diary/register_indirect_labor.html', locals())

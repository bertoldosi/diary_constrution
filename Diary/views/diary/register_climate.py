from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from Diary.forms.diary.climate_form import Climate_form


@login_required(login_url='login')
def Register_climate(request, diary):
    climate_form = Climate_form()
    if request.method == 'POST':
        climate_form = Climate_form(request.POST)
        if climate_form.is_valid():
            climate_form.save()
            return redirect('show_total_service', diary)
        else:
            HttpResponse('Formulário inválido')
    return render(request, 'Diary/diary/register_climate.html', locals())

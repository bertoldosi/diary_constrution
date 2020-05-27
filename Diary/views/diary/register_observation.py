from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from Diary.forms.diary.observation_form import Observation_form


@login_required(login_url='login')
def Register_observation(request, diary):
    observation_form = Observation_form()
    if request.method == 'POST':
        observation_form = Observation_form(request.POST)
        if observation_form.is_valid():
            observation_form.save()
            return redirect('show_diary')
        else:
            HttpResponse('Formulário inválido!')
    return render(request, 'Diary/diary/register_observation.html', locals())

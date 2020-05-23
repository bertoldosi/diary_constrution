from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required(login_url='login')
def Register_engineer(request):
    return render(request, 'Diary/engineer/register_engineer.html', locals())

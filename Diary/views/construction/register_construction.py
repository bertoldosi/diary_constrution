from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required(login_url='login')
def Register_construction(request):
    return render(request, 'Diary/construction/register_construction.html', locals())
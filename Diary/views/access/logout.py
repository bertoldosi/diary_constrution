from django.contrib.auth import logout
from django.shortcuts import render


def Logout(request):
    logout(request)
    return render(request, 'Diary/access/login.html', locals())
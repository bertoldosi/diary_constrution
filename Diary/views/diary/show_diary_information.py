from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required(login_url='login')
def Show_diary_information(request):
    return render(request, 'Diary/diary/show_diary_information.html')
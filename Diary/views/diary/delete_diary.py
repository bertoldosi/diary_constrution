from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from Diary.models import *


@login_required(login_url='login')
def Delete_diary(request, diary_id):
    diary = get_object_or_404(Diary, pk=diary_id)
    diary.delete()
    return redirect('home_page')

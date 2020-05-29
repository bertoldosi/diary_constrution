from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from Diary.models import *


@login_required(login_url='login')
def Delete_user(request, user_id):
    user = get_object_or_404(Access, pk=user_id)
    user.delete()
    return redirect('show_customer')

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from Diary.entidades.engineer import Engineer
from Diary.forms.engineer.register_engineer_form import Engineer_form
from Diary.services import engineer_service


@login_required(login_url='login')
def Register_engineer(request):
    form_engineer = Engineer_form()
    user = request.user.id
    if request.method == 'POST':
        form_engineer = Engineer_form(data=request.POST)
        if form_engineer.is_valid():

            user_access = form_engineer.cleaned_data['user_access']
            engineer_name = form_engineer.cleaned_data['engineer_name']
            engineer_cnpj = form_engineer.cleaned_data['engineer_cnpj']
            engineer_contact = form_engineer.cleaned_data['engineer_contact']
            engineer_street = form_engineer.cleaned_data['engineer_street']
            engineer_number = form_engineer.cleaned_data['engineer_number']
            engineer_city = form_engineer.cleaned_data['engineer_city']
            engineer_state = form_engineer.cleaned_data['engineer_state']
            engineer_cod = form_engineer.cleaned_data['engineer_cod']

            engineer = Engineer(user_access=user_access,
                                engineer_name=engineer_name,
                                engineer_cnpj=engineer_cnpj,
                                engineer_contact=engineer_contact,
                                engineer_street=engineer_street,
                                engineer_number=engineer_number,
                                engineer_city=engineer_city,
                                engineer_state=engineer_state,
                                engineer_cod=engineer_cod,
                                )

            engineer_service.Register_engineer(engineer)

            return redirect('home_page')
    else:
        form_user = Engineer_form()
    return render(request, 'Diary/engineer/register_engineer.html', locals())

from ..models import Engineer


def Register_engineer(engineer):
    engineer = Engineer.objects.create(user_access=engineer.user_access, engineer_name=engineer.engineer_name)

    engineer.save()

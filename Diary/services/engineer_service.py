from ..models import Engineer


def Register_engineer(engineer):
    engineer = Engineer.objects.create(
        user_access=engineer.user_access,
        engineer_name=engineer.engineer_name,
        engineer_cnpj=engineer.engineer_cnpj,
        engineer_contact=engineer.engineer_contact,
        engineer_street=engineer.engineer_street,
        engineer_number=engineer.engineer_number,
        engineer_city=engineer.engineer_city,
        engineer_state=engineer.engineer_state,
        engineer_cod=engineer.engineer_cod,
    )

    engineer.save()

from ..models import Company_user

#meto create_user é especil do modulo AbstractBaseUser da model.
def cadastrar_usuario(usuario):
    usuario = Company_user.objects.create_superuser(
                                         company_user_name=usuario.company_user_name,
                                         company_user_cnpj=usuario.company_user_cnpj,
                                         company_user_responsible=usuario.company_user_responsible,
                                         company_user_contact=usuario.company_user_contact,
                                         company_user_email=usuario.company_user_email,
                                         company_user_address_street=usuario.company_user_address_street,
                                         company_user_address_number=usuario.company_user_address_number,
                                         company_user_address_cod=usuario.company_user_address_cod,
                                         company_user_address_city=usuario.company_user_address_city,
                                         company_user_address_state=usuario.company_user_address_state,
                                         password=usuario.password)
    usuario.save()
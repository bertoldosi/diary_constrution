from ..models import Access


def Register_access(user):
    user = Access.objects.create_user(email=user.email,
                                      user_type=user.user_type,
                                      registration_mode=user.registration_mode,
                                      password=user.password
                                      )
    user.save()

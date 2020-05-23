from ..models import User_access


def Register_user(user):
    user = User_access.objects.create_user(email=user.email, password=user.password)

    user.save()

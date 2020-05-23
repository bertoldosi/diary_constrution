from ..models import User


def Register_user(user):
    user = User.objects.create(user_access=user.user_access, user_name=user.user_name, user_type=user.user_type)

    user.save()
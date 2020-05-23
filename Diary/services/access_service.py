from ..models import Access


def Register_access(user):
    user = Access.objects.create_user(email=user.email, user_type=user.user_type, password=user.password)

    user.save()

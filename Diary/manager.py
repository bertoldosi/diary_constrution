from django.contrib.auth.models import BaseUserManager


class User_manager(BaseUserManager):

    def create_user(self, email, user_type, password, registration_mode):
        if not email:
            raise ValueError('O usuário precisa de email!')
        user = self.model(email=self.normalize_email(email), password=password, user_type=user_type, registration_mode=registration_mode)
        user.set_password(password)
        user.save()
        return user

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from .manager import User_manager


class Access(AbstractBaseUser, PermissionsMixin):
    objects = User_manager()

    email = models.EmailField('Email', unique=True)
    user_type = models.CharField('Tipo', max_length=50)

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['user_type']

    def __str__(self):
        return self.email


class Engineer(models.Model):
    user_access = models.ForeignKey(Access, on_delete=models.CASCADE)

    engineer_name = models.CharField('Nome do engenheiro', max_length=50)

    def __str__(self):
        return self.engineer_name


class Customer(models.Model):
    user_access = models.ForeignKey(Access, on_delete=models.CASCADE)

    customer_name = models.CharField('Nome do cliente', max_length=50)

    def __str__(self):
        return self.customer_name

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

    engineer = models.ForeignKey(Engineer, on_delete=models.CASCADE)

    customer_name = models.CharField('Nome do cliente', max_length=50)

    def __str__(self):
        return self.customer_name


class Construction(models.Model):
    construction_name = models.CharField('Nome da construção', max_length=60)
    construction_date_start = models.DateField('Data de início')
    construction_date_term = models.DateField('Data de entrega')

    construction_company_customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    construction_company_engineer = models.ForeignKey(Engineer, on_delete=models.CASCADE)

    def __str__(self):
        return self.construction_name


class Diary(models.Model):
    diary_date_day = models.DateField('Data do atual')
    diary_construction = models.ForeignKey(Construction, on_delete=models.CASCADE)

    def __str__(self):
        return self.diary_date_day

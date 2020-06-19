from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from .manager import User_manager


class Access(AbstractBaseUser, PermissionsMixin):
    objects = User_manager()

    email = models.EmailField('Email', unique=True)
    user_type = models.CharField('Tipo', max_length=50)
    registration_mode = models.IntegerField('Status do usuario', null=True, blank=True)

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['user_type', 'registration_mode']

    def __str__(self):
        return self.email


class Engineer(models.Model):
    user_access = models.ForeignKey(Access, on_delete=models.CASCADE)

    engineer_name = models.CharField('Nome do engenheiro', max_length=50)
    engineer_cnpj = models.CharField('CNPJ', max_length=50)
    engineer_contact = models.CharField('Número de Contato', max_length=50)
    engineer_street = models.CharField('Rua', max_length=50)
    engineer_number = models.IntegerField('Número')
    engineer_city = models.CharField('Cidade', max_length=50)
    engineer_state = models.CharField('Estado', max_length=50)
    engineer_cod = models.CharField('CEP', max_length=50)

    def __str__(self):
        return self.engineer_name


class Customer(models.Model):
    user_access = models.ForeignKey(Access, on_delete=models.CASCADE)

    engineer = models.ForeignKey(Engineer, on_delete=models.CASCADE)

    customer_name = models.CharField('Nome do cliente', max_length=50)
    customer_cnpj = models.CharField('CNPJ', max_length=50)
    customer_contact = models.CharField('Número de Contato', max_length=50)
    customer_street = models.CharField('Rua', max_length=50)
    customer_number = models.IntegerField('Número')
    customer_city = models.CharField('Cidade', max_length=50)
    customer_state = models.CharField('Estado', max_length=50)
    customer_cod = models.CharField('CEP', max_length=50)

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


class Direct_labor(models.Model):
    direct_labor_description = models.CharField('Mão de obra direta', max_length=40)
    direct_labor_amount = models.IntegerField('Quantidade')

    direct_labor_diary = models.ForeignKey(Diary, on_delete=models.CASCADE)


class Indirect_labor(models.Model):
    indirect_labor_description = models.CharField('Mão de obra indireta', max_length=40)
    indirect_labor_amount = models.IntegerField('Quantidade')

    indirect_labor_diary = models.ForeignKey(Diary, on_delete=models.CASCADE)


class Contractor_labor(models.Model):
    contractor_labor_description = models.CharField('Mão de Obra de Empreiteras', max_length=40)
    contractor_labor_amount = models.IntegerField('Quantidade')

    contractor_labor_diary = models.ForeignKey(Diary, on_delete=models.CASCADE)


class Equipment_construction(models.Model):
    equipment_construction_description = models.CharField('Equipamentos da obra', max_length=40)
    equipment_construction_amount = models.IntegerField('Quantidade')

    equipment_construction_diary = models.ForeignKey(Diary, on_delete=models.CASCADE)


class Contractor_equipment(models.Model):
    contractor_equipment_description = models.CharField('Equipamentos de empreiteiras', max_length=40)
    contractor_equipment_amount = models.IntegerField('Quantidade')

    contractor_equipment_diary = models.ForeignKey(Diary, on_delete=models.CASCADE)


class Climate(models.Model):
    climate_morning = models.CharField('Clima da manhã', max_length=20)
    climate_evening = models.CharField('Clima da tarde', max_length=20)

    climate_diary = models.ForeignKey(Diary, on_delete=models.CASCADE)


class Total_service(models.Model):
    total_service_manpower = models.IntegerField('Quantidade de mão de obra')
    total_service_equipment = models.IntegerField('Quantidade de equipamento')

    total_service_diary = models.ForeignKey(Diary, on_delete=models.CASCADE)


class Observation(models.Model):
    observation_description_service = models.TextField('Descrição do serviço')
    observation_description = models.TextField('Observações')

    observation_diary = models.ForeignKey(Diary, on_delete=models.CASCADE)


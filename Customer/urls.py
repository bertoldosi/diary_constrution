from django.urls import path

from Customer.views import *

app_name = 'customer'

urlpatterns = [
    path('index', Index, name='index'),
    path('register_customer', Register_customer, name='register_customer'),
    path('list_customer', List_customer, name="list_customer"),
    path('edit_customer/<id_customer>', Edit_customer, name="edit_customer"),
    path('change_password', Change_password, name="change_password"),
    path('profile', Profile, name="profile"),
    path('list_project', List_project, name="list_project"),
    path('list_diary/<id_construction>', List_diary, name="list_diary"),
    path('show_diary/<id_diary>', Show_diary, name="show_diary"),
]

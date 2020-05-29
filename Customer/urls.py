from django.urls import path

from Customer.views import Index

app_name = 'customer'

urlpatterns = [
    path('index', Index, name='index'),
]

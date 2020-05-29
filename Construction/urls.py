from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Diary.urls')),
    path('customer/', include('Customer.urls', namespace='customer')),

]

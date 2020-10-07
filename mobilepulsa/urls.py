from django.urls import path

from .views import price_list

app_name = 'mobilepulsa'
urlpatterns = [
    path('', price_list, name='price_list'),
]

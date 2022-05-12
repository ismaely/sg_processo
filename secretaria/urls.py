from django.urls import path
from . import views

app_name = 'secretaria'
urlpatterns = [
    path('registarProcesso', views.registar_processo, name='registar-processo'),
]

from django.urls import path
from . import views

app_name = 'utilizador'
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.loginUser, name='loginUser'),
    path('criarContaUtilizador', views.criarContaUtilizador, name="criar-conta-utilizador"),
]

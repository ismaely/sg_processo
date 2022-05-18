from django.urls import path
from . import views

app_name = 'ajax'
urlpatterns = [
    path('retornaDadosArquivo/', views.retornaDadosArquivo, name="retorna-dados-arquivo"),
]
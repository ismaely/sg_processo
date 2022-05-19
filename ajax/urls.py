from django.urls import path
from . import views

app_name = 'ajax'
urlpatterns = [
    path('retornaDadosArquivo/', views.show_pdf, name="retorna-dados-arquivo"),
]
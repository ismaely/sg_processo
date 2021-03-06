from django.urls import path
from . import views

app_name = 'arquivo'
urlpatterns = [
    path('registarEntradaProcesso', views.registarEntradaProcesso, name='registar-entrada-processo'),
    path('listar_arquivos', views.listar_arquivos, name='listar-arquivos'),
    path('atribuirNumeroProcesso', views.atribuirNumeroProcesso, name='atribuir-numero-processo'),
    path('numeroProcesso/<int:pk>/', views.numeroProcesso, name='numero-processo'),
    path('show_pdf/<int:pk>/', views.show_pdf, name='show-pdf'),
    path('atualizarDados/<int:pk>/', views.atualizarDados, name='atualizar-dados'),
    path('responderArquivo/<int:pk>/', views.responderArquivo, name='responder-arquivo'),
    path('visualizarArquivoResposta/<int:pk>/', views.visualizarArquivoResposta, name='visualizar-arquivo-resposta'),
]

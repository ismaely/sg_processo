from django.shortcuts import render
import random, json
from django.http import JsonResponse, HttpRequest, Http404, HttpResponse
from arquivo.models import Arquivo
# Create your views here.


def retornaDadosArquivo(request):
    try:
        dados = dict()
        if request.method == 'POST':
            
            valor = []
            valor = request.body.decode('utf-8')
            valor = json.loads(valor)
            id = valor['id']
            lista = Arquivo.objects.get(id=int(id))
            dados = {
                'resposta':  lista,
            }
        return JsonResponse(dados)
    except ValueError:
        print(" ERRO RETORNO DOS DADOS DO ARQUIVO")

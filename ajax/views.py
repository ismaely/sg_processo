from django.shortcuts import render
import os
import random, json
from django.http import JsonResponse, HttpRequest,FileResponse, Http404, HttpResponse
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
            dados = {'assunto': lista.assunto, 'descricao':lista.descricao,
            'arquivo': str(lista.arquivo), 'dataEntrada': lista.dataEntrada
            }
            status =200
            
        return JsonResponse(dados)
    except ValueError:
        print(ValueError)
        return JsonResponse({'sucess':False},status=400)


def show_pdf(request):
    filepath = ""
    if request.method == 'POST':
        valor = []
        valor = request.body.decode('utf-8')
        valor = json.loads(valor)
        id = valor['id']
        lista = Arquivo.objects.get(id=int(id))
        file = str(lista.arquivo)

        filepath = os.path.join('media', 'uploads/2022/show.pdf')
        
        return HttpResponse(open(filepath, 'rb'), content_type='application/pdf')


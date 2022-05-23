from django.shortcuts import render
import os
import random, json
from django.http import JsonResponse, HttpRequest,FileResponse, Http404, HttpResponse
from arquivo.models import Arquivo, Resposta
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


def solicitacaoResposta(request):
    try:
        dados = dict()
        if request.method == 'POST':
            valor = []
            valor = request.body.decode('utf-8')
            valor = json.loads(valor)
            id = valor['id']
            lista = Resposta.objects.get(id=int(id))
            if lista.id:
                dados = {'msg': 'Já existe uma solicitação da Resposta, Aguarde!'}
        return JsonResponse(dados)
    except Resposta.DoesNotExist:
        print("novo ----")
        Resposta.objects.create(arquivo_id=id,solicitacao=True)
        dados = {'msg': 'Solicitação feita com sucesso! Aguarde a resposta em breve'}
        return JsonResponse(dados)



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


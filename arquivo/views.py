from multiprocessing import context
from django.http import JsonResponse, HttpRequest,FileResponse,HttpResponse
from django.db.models import Q
import os, json
from django.shortcuts import render
from arquivo.models import Arquivo
from arquivo.forms import  Arquivo_Form, Consultar_form, NumeroProcesso_form



def show_pdf(request, pk):
    filepath = ""
    if pk is not None:
        lista = Arquivo.objects.get(id=int(pk))
        filepath = os.path.join('media', str(lista.arquivo))
        
    return HttpResponse(open(filepath, 'rb'), content_type='application/pdf')


def listar_arquivos(request):
    form = Consultar_form(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            bi = request.POST['numeroIdentificacao']
            categoria = request.POST['categoria']
            estado = request.POST['estado']
            dataEntrada = request.POST['dataEntrada']

            print(dataEntrada)
            
            if bi and categoria and estado and dataEntrada:
                
                lista = Arquivo.objects.select_related('estado').filter(Q(numeroIdentificacao=bi)|Q(tipologia=categoria)|
                Q(estado=estado))
                context = {'lista':lista}
                return render (request, 'arquivos/listarArquivo.html', context)
            
            elif bi and categoria and dataEntrada:
                lista = Arquivo.objects.select_related('estado').filter(Q(numeroIdentificacao=bi)|Q(tipologia=categoria))
                context = {'lista':lista}
                return render (request, 'arquivos/listarArquivo.html', context)
            
            elif bi and estado and dataEntrada:
                lista = Arquivo.objects.select_related('estado').filter(Q(numeroIdentificacao=bi)|Q(estado=estado))
                context = {'lista':lista}
                return render (request, 'arquivos/listarArquivo.html', context)

            elif categoria and estado and dataEntrada:
                
                lista = Arquivo.objects.select_related('estado').filter(Q(tipologia=categoria)|Q(estado=estado))
                context = {'lista':lista}
                return render (request, 'arquivos/listarArquivo.html', context)
           
            elif categoria and dataEntrada:
                
                lista = Arquivo.objects.select_related('estado').filter(Q(tipologia=categoria)|Q(estado=estado))
                context = {'lista':lista}
                return render (request, 'arquivos/listarArquivo.html', context)
            
            elif estado and dataEntrada:
                
                lista = Arquivo.objects.select_related('estado').filter(Q(tipologia=categoria)|Q(estado=estado))
                context = {'lista':lista}
                return render (request, 'arquivos/listarArquivo.html', context)

            elif categoria and estado:
                lista = Arquivo.objects.select_related('estado').filter(Q(tipologia=categoria)|Q(estado=estado))
                context = {'lista':lista}
                return render (request, 'arquivos/listarArquivo.html', context)
            
            elif bi and dataEntrada:
                lista = Arquivo.objects.select_related('estado').filter(QnumeroIdentificacao=bi)
                context = {'lista':lista}
                return render (request, 'arquivos/listarArquivo.html', context)

            elif bi:
                lista = Arquivo.objects.select_related('estado').filter(QnumeroIdentificacao=bi)
                context = {'lista':lista}
                return render (request, 'arquivos/listarArquivo.html', context)
    
    context = {'form':form}
    return render (request, 'arquivos/consultar.html', context)




def atribuirNumeroProcesso(request):
    form = NumeroProcesso_form(request.POST or None)
    if request.method == "POST":
        bi = request.POST['numeroIdentificacao']
        lista = Arquivo.objects.filter(numeroIdentificacao=bi)
        context = {'lista': lista}
        return render (request, 'arquivos/listarNumeroProcesso.html', context)

    context = {'form': form}
    return render (request, 'arquivos/atribuirNumeroProcesso.html', context)


def numeroProcesso(request, pk):
    form = NumeroProcesso_form(request.POST or None)
    if request.method == "POST":
        lista = Arquivo.objects.get(id=pk)
        # lista.numeroProcesso=
        context = {}
        return render (request, 'arquivos/listarNumeroProcesso.html', context)

    context = {'form': form}
    return render (request, 'arquivos/atribuirNumeroProcesso.html', context)




#@login_required -> True if you want to love..
def registarEntradaProcesso(request):
    form = Arquivo_Form(request.POST or None)
    if request.method == "POST":
        form = Arquivo_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            #bi = request.POST['numeroIdentificacao']
            sucesso = True
            context = {'dados':form.cleaned_data, 'sucesso': sucesso}
            return render (request, 'arquivos/reciboEntrada.html', context)
        
    context = {'form': form}
    return render (request, 'arquivos/registarProcesso.html', context)
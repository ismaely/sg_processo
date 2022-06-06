from multiprocessing import context
from django.http import JsonResponse, HttpRequest,FileResponse,HttpResponse,HttpResponseRedirect
from django.db.models import Q
import os, json
from django.urls import reverse
from django.shortcuts import render
from arquivo.models import Arquivo
from arquivo.forms import  Arquivo_Form, Consultar_form, NumeroProcesso_form,Resposta_Form



def show_pdf(request, pk):
    filepath = ""
    context = ""
    if pk is not None:
        lista = Arquivo.objects.get(id=int(pk))
        filepath = os.path.join('media', str(lista.arquivo))
        fs = open(filepath, 'rb')
    return HttpResponse(open(filepath, 'rb'), content_type='application/pdf')


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



def responderArquivo(request, pk):
    form = Resposta_Form(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            print(form.cleaned_data)
            #resp = form.save(commit=False)
            #resp.arquivo = pk
            #resp.save()

    context = {'form': form,'pk':pk}
    return render (request, 'arquivos/responderArquivo.html', context)


def atualizarDados(request, pk):
    sucesso = False
    dados = Arquivo.objects.get(id=int(pk))
    form = Arquivo_Form(request.POST or None, instance=dados)
    context = {'form': form, 'pk':pk}
    if request.method == "POST":
            form = Arquivo_Form(request.POST or None, request.FILES, instance=dados)
            if form.is_valid():
                form.save()
                #context = {'dados':form.cleaned_data, 'sucesso': sucesso}
                #return render (request, 'arquivos/reciboEntrada.html', context)
                #form = Arquivo_Form()
                #context = {'form': form, 'sucesso':True}
                return HttpResponseRedirect(reverse('home:dashboard'))
    return render (request, 'arquivos/registarProcesso.html', context)


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
                
                lista = Arquivo.objects.select_related('estado').filter(Q(numeroIdentificacao=bi)|Q(tipologia=categoria)|Q(estado=estado)|Q(dataEntrada=dataEntrada))
                context = {'lista':lista}
                return render (request, 'arquivos/listarArquivo.html', context)
            
            elif bi and categoria and dataEntrada:
                lista = Arquivo.objects.select_related('estado').filter(Q(numeroIdentificacao=bi)|Q(tipologia=categoria)|Q(dataEntrada=dataEntrada))
                context = {'lista':lista}
                return render (request, 'arquivos/listarArquivo.html', context)
            
            elif bi and estado and dataEntrada:
                lista = Arquivo.objects.select_related('estado').filter(Q(numeroIdentificacao=bi)|Q(estado=estado)|Q(dataEntrada=dataEntrada))
                context = {'lista':lista}
                return render (request, 'arquivos/listarArquivo.html', context)

            elif categoria and estado and dataEntrada:
                
                lista = Arquivo.objects.select_related('estado').filter(Q(tipologia=categoria)|Q(estado=estado))
                context = {'lista':lista}
                return render (request, 'arquivos/listarArquivo.html', context)
           
            elif categoria and dataEntrada:
                
                lista = Arquivo.objects.select_related('estado').filter(Q(tipologia=categoria)|Q(dataEntrada=dataEntrada))
                context = {'lista':lista}
                return render (request, 'arquivos/listarArquivo.html', context)
            
            elif estado and dataEntrada:
                
                lista = Arquivo.objects.select_related('estado').filter(Q(dataEntrada=dataEntrada)|Q(estado=estado))
                context = {'lista':lista}
                return render (request, 'arquivos/listarArquivo.html', context)

            elif categoria and estado:
                lista = Arquivo.objects.select_related('estado').filter(Q(tipologia=categoria)|Q(estado=estado))
                context = {'lista':lista}
                return render (request, 'arquivos/listarArquivo.html', context)
            
            elif bi and dataEntrada:
                lista = Arquivo.objects.select_related('estado').filter(Q(numeroIdentificacao=bi)|Q(dataEntrada=dataEntrada))
                context = {'lista':lista}
                return render (request, 'arquivos/listarArquivo.html', context)

            elif bi:
                lista = Arquivo.objects.select_related('estado').filter(numeroIdentificacao=bi)
                context = {'lista':lista}
                return render (request, 'arquivos/listarArquivo.html', context)
            
            elif estado:
                lista = Arquivo.objects.select_related('estado').filter(estado=estado)
                context = {'lista':lista}
                return render (request, 'arquivos/listarArquivo.html', context)
    
    context = {'form':form}
    return render (request, 'arquivos/consultar.html', context)




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
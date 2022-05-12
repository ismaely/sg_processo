from multiprocessing import context
from django.db.models import Q
from django.shortcuts import render
from arquivo.models import Arquivo
from arquivo.forms import  Arquivo_Form, Consultar_form





def listar_arquivos(request):
    form = Consultar_form(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            bi = request.POST['numeroIdentificacao']
            categoria = request.POST['categoria']
            estado = request.POST['estado']
            
            if bi and categoria and estado:
                
                lista = Arquivo.objects.select_related('estado').filter(Q(numeroIdentificacao=bi)|Q(tipologia=categoria)|
                Q(estado=estado))
                context = {'lista':lista}
                return render (request, 'arquivos/listarArquivo.html', context)
            
            elif bi and categoria:
                print("certo-------")
                lista = Arquivo.objects.select_related('estado').filter(Q(numeroIdentificacao=bi)|Q(tipologia=categoria))
                context = {'lista':lista}
                return render (request, 'arquivos/listarArquivo.html', context)
            elif bi and estado:
                lista = Arquivo.objects.select_related('estado').filter(Q(numeroIdentificacao=bi)|Q(estado=estado))
                context = {'lista':lista}
                return render (request, 'arquivos/listarArquivo.html', context)

            elif categoria and estado:
                
                lista = Arquivo.objects.select_related('estado').filter(Q(tipologia=categoria)|Q(estado=estado))
                context = {'lista':lista}
                return render (request, 'arquivos/listarArquivo.html', context)
            elif bi:
                lista = Arquivo.objects.select_related('estado').filter(QnumeroIdentificacao=bi)
                
                context = {'lista':lista}
                return render (request, 'arquivos/listarArquivo.html', context)
    
    context = {'form':form}
    return render (request, 'arquivos/consultar.html', context)



def atribuirNumeroProcesso(request):
    form = Consultar_form(request.POST or None)
    if request.method == "POST":
        nome = request.POST['nome'].upper()
        lista = Arquivo.objects.filter(Q(titulo__contains=nome) | Q(autor__contains=nome))
        context = {'lista': lista}
        return render (request, 'arquivos/listar_arquivos.html', context)

    context = {'form': form}
    return render (request, 'arquivos/atribuirNumeroProcesso.html', context)





#@login_required -> True if you want to love..
def registarEntradaProcesso(request):
    form = Arquivo_Form(request.POST or None)
    if request.method == "POST":
        form = Arquivo_Form(request.POST, request.FILES)
        if form.is_valid():
            bi = request.POST['numeroIdentificacao']
            sucesso = True
            context = {'dados':form.cleaned_data, 'sucesso': sucesso}
            return render (request, 'arquivos/reciboEntrada.html', context)
        
    context = {'form': form}
    return render (request, 'arquivos/registarProcesso.html', context)
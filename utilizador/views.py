from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import check_password
from django.contrib import messages
from django.urls import reverse, path
from environment.env import SENHA_PADRAO
from utilizador.forms import Utilizador_Form, User_Form, LoginForm
from config.views import prepara_foto
from utilizador.models import Utilizador


def index(request):
    form = LoginForm(request.POST or None)
    if request.method == 'POST':
        try:
            if form.is_valid():
                senha = form.cleaned_data.get('senha')
                nome = form.cleaned_data.get('username')
                resp = User.objects.get(username=nome)
                password = check_password(senha, resp.password)
                if resp.username == nome and password:
                    conta = Utilizador.objects.get(user_id=resp.id)
                    if resp.is_active:
                        if int(conta.estado) == 1:
                            user = authenticate(username=nome, password=senha)
                            login(request, user)
                            request.session.set_expiry(31000) # a session vai terminar em 24 horas
                            return HttpResponseRedirect(reverse('home:dashboard'))
                        else:
                            return HttpResponseRedirect(reverse('utilizador:troca-senha-padrao'))
                    else:
                        #sweetify.info(
                        #request, 'A Conta esta desativada <br> Diriga-se ao Administrador!.', persistent='OK')
                        return HttpResponseRedirect(reverse('utilizador:sair'))
               
        except User.DoesNotExist:
            messages.warning(request, 'A conta não existe...')

    context = {'form':form}
    return render (request, 'utilizador/index.html', context)


def loginUser(request):
    context = {}
    return render (request, 'utilizador/login.html', context)


#@login_required
def criarContaUtilizador(request):
    form = User_Form(request.POST or None)
    form2 = Utilizador_Form(request.POST or None)
    sucesso = False
    if request.method == 'POST':
        form2 = Utilizador_Form(request.POST, request.FILES or None)
        if form.is_valid() and form2.is_valid():
            foto = form2.cleaned_data.get('foto')
            email = request.POST['email']
            nome=request.POST['nome']
            categoria=request.POST['categoria']
            user = User.objects.create_user(username=nome, first_name=categoria,email=email, password=SENHA_PADRAO)
            
            utilizador = form2.save(commit=False)
            if len(foto) > 0:
                utilizador.foto = prepara_foto(request)
            else:
                utilizador.foto ='user.jpg'

            utilizador.user_id = user.id
            utilizador.save()
            sucesso = True
            form = User_Form()
            form2 = Utilizador_Form()
            """subject = 'PREI - CONTA CRIADA'
            message = 'A sua conta foi criada com sucesso sua Password: 2022.Prei@'
            from_email = settings.EMAIL_HOST_USER
            recipient_list = email
            send_mail(subject, message, from_email, [recipient_list ], fail_silently=False)
            """
            

    context = {'form':form, 'form2':form2,'sucesso':sucesso}
    return render (request, 'utilizador/criarContaUtilizador.html', context)
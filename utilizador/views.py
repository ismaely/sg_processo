from django.shortcuts import render
from django.contrib.auth.models import User
from environment.env import SENHA_PADRAO
from utilizador.forms import Utilizador_Form, User_Form, LoginForm
from config.views import prepara_foto


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
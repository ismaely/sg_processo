from django import forms
from django.forms import ModelForm
from utilizador.models import Entidade, Utilizador, Categoria



CATEGORIA = []
ENTIDADE = []
for res in Entidade.objects.all():
    ENTIDADE.append([int(res.id), str(res.nome)])


for res in Categoria.objects.all():
    CATEGORIA.append([int(res.id), str(res.nome)])


class Utilizador_Form(ModelForm):
    ndi = forms.CharField(max_length=40, widget=forms.TextInput(attrs={'class': 'form-control maiuscula'}))
    telefone = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'form-control'}))
    foto = forms.CharField(required=False, widget=forms.TextInput(attrs={'type':'hidden', 'class': 'form-control', 'id': 'fotoSalva'}))
    class Meta:
        model = Utilizador
        fields = ['telefone','ndi', 'foto']
        widgets = {
            #'genero': forms.Select( attrs={'class': 'form-control'}),
        }



class User_Form(forms.Form):
    nome = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control '}))
    categoria = forms.CharField(max_length=160, widget=forms.Select(choices=CATEGORIA, attrs={'class': 'form-control'}))
    password = forms.CharField(max_length=30,required=False, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(max_length=180, required=False, widget=forms.TextInput(attrs={'class': 'form-control', }))


class LoginForm(forms.Form):
    senha = forms.CharField(max_length=20, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    username = forms.CharField(max_length=80, widget=forms.TextInput(attrs={'class': 'form-control'}))


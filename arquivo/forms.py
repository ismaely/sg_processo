from django import forms
from django.forms import ModelForm
from arquivo.models import Arquivo, Topologia, Estado



CATEGORIA = []
ESTADO = []


CATEGORIA.append(['', '---------'])
for x in Topologia.objects.all():
    CATEGORIA.append([int(x.id), str(x.nome)])


ESTADO.append(['', '---------'])
for x in Estado.objects.all():
    ESTADO.append([int(x.id), str(x.nome)])
 

class Arquivo_Form(ModelForm):
    assunto = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control '}))
    numero_pagina = forms.CharField(max_length=40,required=False, widget=forms.TextInput(attrs={'class': 'form-control maiuscula'}))
    numeroIdentificacao = forms.CharField(max_length=40, widget=forms.TextInput(attrs={'class': 'form-control maiuscula'}))
    autor = forms.CharField(max_length=50, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    telefone = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'form-control'}))
    numeroProcesso = forms.CharField(max_length=180, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    destinatario = forms.CharField(max_length=60,required=False,  widget=forms.TextInput( attrs={'class': 'form-control'}))
    arquivo = forms.FileField(required=False, widget=forms.TextInput(attrs={'type': 'file', 'class': 'form-control'}))
    descricao = forms.CharField(max_length=510, widget=forms.Textarea(attrs={ 'class': 'form-control '}))
    class Meta:
        model = Arquivo
        fields = ['tipologia','estado', 'departamentoDestino', 'dataEntrada','descricao',
         'assunto', 'numero_pagina','autor','numeroProcesso', 'destinatario','numeroIdentificacao', 'arquivo']

        widgets = {
            'tipologia': forms.Select(attrs={'class': 'form-control'}),
            'estado': forms.Select( attrs={'class': 'form-control'}),
            'departamentoDestino': forms.Select( attrs={'class': 'form-control'}),
            'dataEntrada': forms.DateInput(attrs={'type': 'date','class': 'form-control'}),
        }





class Consultar_form(forms.Form):
    numeroIdentificacao = forms.CharField(max_length=10,required=False, widget=forms.TextInput(attrs={'class': 'form-control '}))
    categoria = forms.CharField(max_length=160,required=False, widget=forms.Select(choices=CATEGORIA, attrs={'class': 'form-control'}))
    estado = forms.CharField(max_length=160,required=False, widget=forms.Select(choices=ESTADO, attrs={'class': 'form-control'}))
    
    
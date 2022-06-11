from django import forms
from django.forms import ModelForm
from arquivo.models import Arquivo, Topologia, Estado, Resposta, Departamento



CATEGORIA = []
ESTADO = []
DEPARTAMENTO = []


CATEGORIA.append(['', '---------'])
for x in Topologia.objects.all():
    CATEGORIA.append([int(x.id), str(x.nome)])


ESTADO.append(['', '---------'])
for x in Estado.objects.all():
    ESTADO.append([int(x.id), str(x.nome)])


DEPARTAMENTO.append(['', '---------'])
for x in Departamento.objects.all():
    DEPARTAMENTO.append([int(x.id), str(x.nome)])
 

class Arquivo_Form(ModelForm):
    assunto = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control '}))
    numero_pagina = forms.CharField(max_length=40,required=False, widget=forms.TextInput(attrs={'class': 'form-control maiuscula'}))
    numeroIdentificacao = forms.CharField(max_length=40, required=False,widget=forms.TextInput(attrs={'class': 'form-control maiuscula'}))
    autor = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    telefone = forms.CharField(max_length=30,required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    numeroProcesso = forms.CharField(max_length=180, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    destinatario = forms.CharField(max_length=60,required=False,  widget=forms.TextInput( attrs={'class': 'form-control'}))
    arquivo = forms.FileField(required=False, widget=forms.FileInput(attrs={'type': 'file', 'class': 'form-control'}))
    descricao = forms.CharField(max_length=510,required=False, widget=forms.Textarea(attrs={ 'class': 'form-control '}))
    foto = forms.CharField(required=False, widget=forms.TextInput(attrs={'type':'hidden', 'class': 'form-control', 'id': 'fotoSalva'}))
    class Meta:
        model = Arquivo
        fields = ['tipologia','estado', 'departamentoDestino', 'dataEntrada','descricao','assunto', 'numero_pagina',
         'autor','numeroProcesso', 'destinatario','numeroIdentificacao', 'arquivo', 'foto']

        widgets = {
            'tipologia': forms.Select(attrs={'class': 'form-control'}),
            'estado': forms.Select( attrs={'class': 'form-control'}),
            'departamentoDestino': forms.Select( attrs={'class': 'form-control'}),
            'dataEntrada': forms.DateInput(attrs={'type': 'date','class': 'form-control'}),
        }



class Resposta_Form(ModelForm):
    titulo = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control '}))
    msg = forms.CharField(max_length=10990, widget=forms.Textarea(attrs={ 'class': 'form-control html-editor', 'rows':'12'}))
    arquivo = forms.CharField(max_length=4, required=False, widget=forms.TextInput(attrs={'class': 'form-control '}))
    departamentoDestino = forms.CharField(max_length=160, widget=forms.Select(choices=DEPARTAMENTO, attrs={'class': 'form-control'}))
    class Meta:
        model = Resposta
        fields = ['tipoResposta','dataEntrada','msg', 'titulo']

        widgets = {
            'tipoResposta': forms.Select(attrs={'class': 'form-control'}),
            'dataEntrada': forms.DateInput(attrs={'type': 'date','class': 'form-control'}),
        }

    """def clean_msg(self):
        msg = self.cleaned_data.get('msg')
        max_file_size = 10840
        if int(nota_final) > 9 and int(nota_final) <= 20:
            return nota_final
        else:
            raise forms.ValidationError("A media final não é valida")"""

class Consultar_form(forms.Form):
    numeroIdentificacao = forms.CharField(max_length=10,required=False, widget=forms.TextInput(attrs={'class': 'form-control '}))
    categoria = forms.CharField(max_length=160,required=False, widget=forms.Select(choices=CATEGORIA, attrs={'class': 'form-control'}))
    estado = forms.CharField(max_length=160,required=False, widget=forms.Select(choices=ESTADO, attrs={'class': 'form-control'}))
    dataEntrada = forms.CharField(max_length=20,required=False, widget=forms.TextInput(attrs={'type': 'date','class': 'form-control'}))
    
  
class NumeroProcesso_form(forms.Form):
    numeroIdentificacao = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'form-control '}))
   
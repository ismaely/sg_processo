from django.db import models
from django.utils import timezone

# Create your models here.


class Topologia(models.Model):
    nome = models.CharField(max_length=100)
    detalhe = models.CharField(max_length=100, blank=True, null=True)
    def __str__ (self):
        return self.nome


class Estado(models.Model):
    nome = models.CharField(max_length=100)
    detalhe = models.CharField(max_length=100, blank=True, null=True)
    def __str__ (self):
        return self.nome


class Departamento(models.Model):
    nome = models.CharField(max_length=100)
    detalhe = models.CharField(max_length=100, blank=True, null=True)
    def __str__ (self):
        return self.nome


class Arquivo(models.Model):
    tipologia = models.ForeignKey(Topologia, on_delete=models.CASCADE, parent_link=True)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE, parent_link=True)
    assunto = models.CharField(max_length=100)
    autor = models.CharField(max_length=70, blank=True, null=True)
    numero_pagina = models.CharField(max_length=5, null=True, blank=True, default="")
    destinatario = models.CharField(max_length=70, blank=True, null=True)
    departamentoDestino = models.ForeignKey(Departamento, on_delete=models.CASCADE, parent_link=True)
    descricao = models.CharField(max_length=670, blank=True, null=True)
    numeroProcesso = models.CharField(max_length=20, blank=True, null=True)
    arquivo = models.FileField(upload_to="uploads/%Y/",blank=True, null=True)
    dataEntrada = models.DateField(default=timezone.now)
    created = models.DateField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)
    numeroIdentificacao = models.CharField(max_length=20, blank=True, null=True)
    foto = models.ImageField(upload_to='fotos/', blank=True, null=True, default="user.jpg")
    class Meta:
        ordering = ['assunto']
    def __str__ (self):
        return self.id
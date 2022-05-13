from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Categoria(models.Model):
    nome = models.CharField(max_length=150)
    sigla = models.CharField(max_length=60, blank=True, null=True, default=" ")

    def __str__(self):
        return "%s" % (self.nome)


class Entidade(models.Model):
    nome = models.CharField(max_length=100)
    sigla = models.CharField(max_length=90, blank=True, null=True, default=" ")
    descricao = models.CharField(max_length=190, blank=True, null=True, default=" ")
    def __str__(self):
        return "%s" % (self.nome)


class Utilizador(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE, parent_link=True)
    ndi = models.CharField(max_length=40)
    telefone = models.CharField(max_length=50,blank=True, null=True)
    foto = models.ImageField(upload_to='user/', blank=True, null=True, default="user.jpg")
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    def __str__ (self):
        return '%d' % (self.id)
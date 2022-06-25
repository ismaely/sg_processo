import random, base64
from django.utils import timezone
from utilizador.models import Categoria, Entidade

DATA_HORA_ZONA = timezone.now()
DATA_ANO = timezone.now().year
SENHA_PADRAO = '2022.marinha'

CATEGORIA = []
ENTIDADE = []

for res in Entidade.objects.all():
    ENTIDADE.append([int(res.id), str(res.nome)])

for res in Categoria.objects.all():
    CATEGORIA.append([int(res.id), str(res.nome)])

from django.shortcuts import render
import random, base64
from environment.env import DATA_HORA_ZONA, DATA_ANO
# Create your views here.

# FUNÇÃO QUE VAI PREPARAR A FOTO Q SERA SALVA,  E QUE VVAI GUARDAR NA PASTA DE FOTOS
def prepara_foto(request):
    img = request.POST["foto"]
    nome = str(DATA_HORA_ZONA).split('.')
    foto = []
    inicio = img.find(',')
    imagem = img[inicio+1:]

    with open("./media/fotos/"+ str(nome[0]) + "_" + str(random.random()) + ".png", "wb") as fh:
        fh.write(base64.b64decode(imagem))
        foto = str(fh).split('=')
        um = foto[1].replace(">", '')

    um = um.replace("'", '')
    um = um.split('media/')
    return um[1]

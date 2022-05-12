from django.shortcuts import render

# Create your views here.


def registar_processo(request):
    context = {}
    return render (request, 'home/home.html', context)
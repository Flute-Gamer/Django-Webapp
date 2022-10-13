from django.shortcuts import render

# Create your views here.

def login(request):
    return render(request, "login.html")

def inicial(request):
    return render(request, "inicial.html")

def cadastroVoos(request):
    return render(request, "cadastroVoos.html")

def relatorios(request):
    return render(request, "relatorios.html")

def monitoraVoos(request):
    return render(request, "monitoraVoos.html")
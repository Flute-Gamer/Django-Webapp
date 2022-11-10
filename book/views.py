from django.shortcuts import render
import datetime
# Create your tests here.
from book.class_voo import Voo

def login(request):
    return render(request, "login.html")

def inicial(request):
    return render(request, "inicial.html")

def cadastroVoos(request):
    return render(request, "cadastroVoos.html")

def relatorios(request):
    return render(request, "relatorios.html")

def monitoraVoos(request):
    voo_1 = mostraVoos(request)
    context = {
        'voo_mostrado': voo_1
    }
    return render(request, "monitoraVoos.html", context)

def mostraVoos(request):
    voo = Voo(0,"Passos","Curitiba ou Passos",datetime.date(2022,11,11),datetime.date(2022,11,12))
    print('codigo '+ str(voo.get_codigo_de_voo()))
    return ('codigo '+ str(voo.get_codigo_de_voo()))
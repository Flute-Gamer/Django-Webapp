import io
from django.shortcuts import render
import datetime
# Create your tests here.
from book.class_voo import Voo
from django.http import FileResponse

from book.class_GeradorRelatorio import GeradorRelatorio
# Create your views here.

def login(request):
    return render(request, "login.html")

def inicial(request):
    return render(request, "inicial.html")

def cadastroVoos(request):
    return render(request, "cadastroVoos.html")

def relatorios(request):
    retornaRelatorioPDF(request)
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


def retornaRelatorioPDF(request):
    buffer = io.BytesIO()
    buffer.seek(0)
    relatorio = GeradorRelatorio(None,None,None)
    relatorio.gera_pdf()
    return FileResponse(buffer, as_attachment=True, filename='requirements.txt')


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
    context = {
        'voo_mostrado': mostra_codigo_do_voo(request),
        'status_mostrado': mostra_status_do_voo(request),
        'destino_mostrado': mostra_aeroporto_destino(request),
        'partida_mostrada': mostra_aeroporto_partida(request)
    }
    return render(request, "monitoraVoos.html", context)

def mostra_codigo_do_voo(request):
    voo = Voo(0,"Passos","Curitiba ou Passos",datetime.date(2022,11,11),datetime.date(2022,11,12))
    print('Código do voo: '+ str(voo.get_codigo_de_voo()))
    return ('Código do voo: '+ str(voo.get_codigo_de_voo()))

def mostra_status_do_voo(request):
    voo = Voo(0,"Passos","Curitiba ou Passos",datetime.date(2022,11,11),datetime.date(2022,11,12))
    print('Status do voo: '+ str(voo.get_status()))
    return ('Status do voo: '+ str(voo.get_status()))

def mostra_aeroporto_destino(request):
    voo = Voo(0,"Passos","Curitiba ou Passos",datetime.date(2022,11,11),datetime.date(2022,11,12))
    print('Destino do voo: '+ str(voo.get_aeroporto_destino()))
    return ('Destino do voo: '+ str(voo.get_aeroporto_destino()))

def mostra_aeroporto_partida(request):
    voo = Voo(0,"Passos","Curitiba ou Passos",datetime.date(2022,11,11),datetime.date(2022,11,12))
    print('Partida do voo: '+ str(voo.get_aeroporto_partida()))
    return ('Partida do voo: '+ str(voo.get_aeroporto_partida()))


def retornaRelatorioPDF(request):
    buffer = io.BytesIO()
    buffer.seek(0)
    relatorio = GeradorRelatorio(None,None,None)
    relatorio.gera_pdf()
    return FileResponse(buffer, as_attachment=True, filename='requirements.txt')


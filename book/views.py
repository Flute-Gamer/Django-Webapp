import io
from django.shortcuts import render
import datetime
# Create your tests here.
from book.class_voo import Voo
from django.http import FileResponse

from book.class_GeradorRelatorio import GeradorRelatorio
from book.forms import Formulario_Cadastro_Voo
# Create your views here.

def login(request):
    return render(request, "login.html")

def inicial(request):
    return render(request, "inicial.html")

def cadastroVoos(request):
    if request.method == "GET":
        form = Formulario_Cadastro_Voo()
        context = {
            'form' : form
        }
        return render(request, "cadastroVoos.html", context)
    else:
        form = Formulario_Cadastro_Voo(request.POST)
        print (form.data['destino_do_voo'])
        context = {}
        return render(request, "cadastroVoos.html", context)

def relatorios(request):
    retornaRelatorioPDF(request)
    return render(request, "relatorios.html")

def monitoraVoos(request):
    context = {
        'voo_mostrado': mostra_codigo_do_voo(request),
        'status_mostrado': mostra_status_do_voo(request),
        'destino_mostrado': mostra_aeroporto_destino(request),
        'partida_mostrada': mostra_aeroporto_partida(request),
        'partida_prevista' : mostra_partida_prevista(request),
        'partida_real' : mostra_partida_real(request),
        'chegada_prevista' : mostra_chegada_prevista(request),
        'chegada_real' : mostra_chegada_real(request)
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

def mostra_partida_prevista(request):
    voo = Voo(0,"Passos","Curitiba ou Passos",datetime.date(2022,11,11),datetime.date(2022,11,12))
    print('Partida prevista: '+ str(voo.get_partida_prevista()))
    return ('Partida prevista: '+ str(voo.get_partida_prevista()))

def mostra_partida_real(request):
    voo = Voo(0,"Passos","Curitiba ou Passos",datetime.date(2022,11,11),datetime.date(2022,11,12))
    print('Partida real: '+ str(voo.get_partida_real()))
    return ('Partida real: '+ str(voo.get_partida_real()))

def mostra_chegada_prevista(request):
    voo = Voo(0,"Passos","Curitiba ou Passos",datetime.date(2022,11,11),datetime.date(2022,11,12))
    print('Chegada prevista: '+ str(voo.get_chegada_prevista()))
    return ('Chegada prevista: '+ str(voo.get_chegada_prevista()))

def mostra_chegada_real(request):
    voo = Voo(0,"Passos","Curitiba ou Passos",datetime.date(2022,11,11),datetime.date(2022,11,12))
    print('Chegada real: '+ str(voo.get_chegada_real()))
    return ('Chegada real: '+ str(voo.get_chegada_real()))


def retornaRelatorioPDF(request):
    buffer = io.BytesIO()
    buffer.seek(0)
    
    relatorio = GeradorRelatorio(None, None, None) #GeradorRelatorio(tipo, inicio, fim)
    #                 tipo é um boolean (0 para Partidas e 1 para Chegadas)
    #                 inicio e fim sao datetimes na forma AAAA/MM/DD-HH:MM:SS
    
    relatorio.gera_pdf() #funcao que gera pdf a paritr do objeto instanciado acima da classe
    return FileResponse(open('test.pdf','rb'))

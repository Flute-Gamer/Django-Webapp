import datetime
import io

# Create your tests here.
# from book.class_voo import Voo
from django.http import FileResponse
from django.shortcuts import render

from book.class_GeradorRelatorio import GeradorRelatorio
from book.forms import Codigo_Voo_Monitora, Formulario_Cadastro_Voo
from book.models import Voo
from django.http.response import HttpResponse

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
        if form.is_valid():
            print (form.cleaned_data)
            
            codigo = form.cleaned_data['código_do_voo']
            verifica_codigo = Voo.objects.filter(codigo_de_voo=codigo).first()
            if verifica_codigo:                 ##IF que nao deixa criar dois voos com mesmo código
                return HttpResponse('Já existe um voo com esse código')
            
            destino = form.cleaned_data['destino_do_voo']
            origem = form.cleaned_data['origem_do_voo'] 
            partida_prev = form.cleaned_data['partida_prevista'] 
            chegada_prev = form.cleaned_data['chegada_prevista'] 
            print('DESTINO: ' + str(destino))
            Voo.objects.create(
            codigo_de_voo=codigo,
            aeroporto_destino=destino,
            aeroporto_partida=origem,
            partida_prevista=partida_prev,
            chegada_prevista=chegada_prev,
            status=1
            )
                #Refresh
                #Error msg
    
        context = {
            'form' : form
        }
        return render(request, "cadastroVoos.html", context)

def relatorios(request):
    # Simplesmente renderização, quem manipula a criação do relatório é o html relatorios.html, na function downloadRelatorio()
    return render(request, "relatorios.html")

def escolheVooMonitorado(request):
    # Receptor dos dados usados em `monitoraVoos()`
    if request.method == "GET":
        form = Codigo_Voo_Monitora()
        context = {
            'form' : form
        }
        return render(request, "escolheVoo.html")

        
    else:
        form = Codigo_Voo_Monitora(request.POST)
        if form.is_valid():
            print (form.cleaned_data)    
        context = {
            'form' : form
        }
        monitoraVoos(request,form.cleaned_data['codigo_voo'])

def monitoraVoos(request,codigo_voo):
    # Como queries são feitas hardcoded, utilizar forms (Útil no desenvolvimento da busca em outras )
    context = {
        'voo_mostrado': mostra_codigo_do_voo(5),
        'status_mostrado': mostra_status_do_voo(5),
        'destino_mostrado': mostra_aeroporto_destino(5),
        'partida_mostrada': mostra_aeroporto_partida(5),
        'partida_prevista' : mostra_partida_prevista(5),
        'partida_real' : mostra_partida_real(5),
        'chegada_prevista' : mostra_chegada_prevista(5),
        'chegada_real' : mostra_chegada_real(5)
    }
    return render(request, "monitoraVoos.html", context)

def mostra_codigo_do_voo(codigo_voo):
    voo = Voo.objects.get(codigo_de_voo=codigo_voo)
    print('Código do voo: '+ str(voo.codigo_de_voo))
    return ('Código do voo: '+ str(voo.codigo_de_voo))

def mostra_status_do_voo(codigo_voo):
    voo = Voo.objects.get(codigo_de_voo=codigo_voo)
    print('Status do voo: '+ str(voo.status))
    return ('Status do voo: '+ str(voo.status))

def mostra_aeroporto_destino(codigo_voo):
    voo = Voo.objects.get(codigo_de_voo=codigo_voo)
    print('Destino do voo: '+ str(voo.aeroporto_destino))
    return ('Destino do voo: '+ str(voo.aeroporto_destino))

def mostra_aeroporto_partida(codigo_voo):
    voo = Voo.objects.get(codigo_de_voo=codigo_voo)
    print('Partida do voo: '+ str(voo.aeroporto_partida))
    return ('Partida do voo: '+ str(voo.aeroporto_partida))

def mostra_partida_prevista(codigo_voo):
    voo = Voo.objects.get(codigo_de_voo=codigo_voo)
    print('Partida prevista: '+ str(voo.partida_prevista))
    return ('Partida prevista: '+ str(voo.partida_prevista))

def mostra_partida_real(codigo_voo):
    voo = Voo.objects.get(codigo_de_voo=codigo_voo)
    print('Partida real: '+ str(voo.partida_real))
    return ('Partida real: '+ str(voo.partida_real))

def mostra_chegada_prevista(codigo_voo):
    voo = Voo.objects.get(codigo_de_voo=codigo_voo)
    print('Chegada prevista: '+ str(voo.chegada_prevista))
    return ('Chegada prevista: '+ str(voo.chegada_prevista))

def mostra_chegada_real(codigo_voo):
    voo = Voo.objects.get(codigo_de_voo=codigo_voo)
    print('Chegada real: '+ str(voo.chegada_real))
    return ('Chegada real: '+ str(voo.chegada_real))


def retornaRelatorioPDF(request):
    #buffer = io.BytesIO()
    #buffer.seek(0)          #Linhas inúteis
    
    relatorio = GeradorRelatorio(None, None, None) #GeradorRelatorio(tipo, inicio, fim)
    #                 tipo é um boolean (0 para Partidas e 1 para Chegadas)
    #                 inicio e fim sao datetimes na forma AAAA/MM/DD-HH:MM:SS 
    #                 (Utilizar a seguinte parte da documentação: https://docs.djangoproject.com/en/4.1/ref/forms/fields/#datetimefield )
    
    arquivo = relatorio.gera_pdf() #funcao que gera pdf a paritr do objeto instanciado acima da classe
    return FileResponse(open(arquivo,'rb'))

import io
import json
from urllib.parse import urlencode
from django.shortcuts import redirect, render
from django.contrib import messages
from django.http import FileResponse
from django.shortcuts import render
from book.class_GeradorRelatorio import GeradorRelatorio
from book.forms import Codigo_Voo_Monitora, DateTimeField_ERelatorio, Formulario_Cadastro_Voo
from book.models import Voo
from django.http.response import HttpResponse
from django.contrib.auth import authenticate, login

# Create your views here.

def login(request):
    if request.method == 'GET':
        return render(request, "login.html")
    else:
        if "load_count" in request.session:
            count = request.session["load_count"] + 1
        else:
            count = 1

        request.session["load_count"] = count
        usuario = request.POST.get('login')
        senha = request.POST.get('senha')

        user = authenticate(usuario=usuario, senha=senha)
        if user:
            login(request, user)
            return HttpResponse('Autenticado')
        else:
            context = {'i':count}
            print(count)
            if count < 3:
                messages.success(request, 'Usuário ou senha inválidas.')
                parameters = urlencode(context)
                return redirect(f'../login/auth?{parameters}')
            else:
                messages.success(request, 'Usuário ou senha inválidas.')
                return render(request, "login_fail.html")


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
                messages.success(request, 'Já existe voo com esse código de voo.')
                context = {
                    'form' : form
                 }
                return render(request, "cadastroVoos.html", context)
            
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
        messages.success(request, 'Voo cadastrado com sucesso.')
        context = {
            'form' : form
        }
        return render(request, "cadastroVoos.html", context)

def relatorios(request):
    # Simplesmente renderização, quem manipula a criação do relatório é o html relatorios.html, na function downloadRelatorio()
    if request.method == "GET":
        form = DateTimeField_ERelatorio()
        context = {
            'form' : form
        }
        return render(request, "relatorios.html",context)

        
    else:
        form = DateTimeField_ERelatorio(request.POST)
        if form.is_valid():
            print (form.cleaned_data)    
        context = {
            'form' : form
        }
        data_inicio = form.cleaned_data['data_inicio']
        data_fim = form.cleaned_data['data_fim']
        tipo_relatorio =  form.cleaned_data['tipo']
        retornaRelatorioPDF(request,tipo_relatorio,data_inicio,data_fim)
        return render(request, "relatorios.html",context)

def escolheVooMonitorado(request):
    # Receptor dos dados usados em `monitoraVoos()`
    if request.method == "GET":
        form = Codigo_Voo_Monitora()
        context = {
            'form' : form
        }
        return render(request, "escolheVoo.html",context)

        
    else:
        form = Codigo_Voo_Monitora(request.POST)
        if form.is_valid():
            print (form.cleaned_data)    
        context = {
            'form' : form
        }
        if Voo.objects.filter(codigo_de_voo=form.cleaned_data['codigo_voo']).exists():
            parameters = urlencode(form.cleaned_data)
            return redirect(f'monitoraVoos/vooEscolhido?{parameters}')
        else:
            messages.success(request, 'Código de Voo inexistente.')
            return render(request, "escolheVoo.html",context)

def monitoraVoos(request):
    if request.method == "GET":
        form = Codigo_Voo_Monitora()
        print(request.get_full_path())
        codigo_voo=request.get_full_path()
        codigo_voo=codigo_voo.split('=')[1]
        print(codigo_voo)
        context = {
            'voo_mostrado': mostra_codigo_do_voo(codigo_voo),
            'status_mostrado': mostra_status_do_voo(codigo_voo),
            'destino_mostrado': mostra_aeroporto_destino(codigo_voo),
            'partida_mostrada': mostra_aeroporto_partida(codigo_voo),
            'partida_prevista' : mostra_partida_prevista(codigo_voo),
            'partida_real' : mostra_partida_real(codigo_voo),
            'chegada_prevista' : mostra_chegada_prevista(codigo_voo),
            'chegada_real' : mostra_chegada_real(codigo_voo),
            'form' : form
        }
        return render(request, "monitoraVoos.html", context)
    
    else:
        print("entrou no else")
        form = Formulario_Cadastro_Voo(request.POST)
        print("chegou aqui")
        if form.is_valid():
            print (form.cleaned_data)
            
            codigo = form.cleaned_data['código_do_voo']
            verifica_codigo = Voo.objects.filter(codigo_voo=codigo).exists()
            print(verifica_codigo)
            if verifica_codigo:                 ##IF que deleta se código está na basa de dados
                deleta_voo(codigo)
                print("Deletou")
                print("passou 2")
                messages.success(request, 'Voo deletado com sucesso.')
                context = {
                    'form' : form
                 }
                return render(request, "monitoraVoos.html", context)
            
            else:
                print("passou")
                messages.success(request, 'Voo não encontrado na nossa base de dados.')
                context = {
                        'form' : form
                    }
                return render(request, "monitoraVoos.html", context)

def deleta_voo(codigo_voo):
    voo =  Voo.objects.get(codigo_de_voo=codigo_voo)
    voo.chegada_real.delete()
    voo.chegada_prevista.delete()
    voo.partida_real.delete()
    voo.partida_prevista.delete()
    voo.aeroporto_partida.delete()
    voo.aeroporto_destino.delete()
    voo.status.delete()
    voo.codigo_de_voo.delte()
    return

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


def retornaRelatorioPDF(request,tipo,data_inicio,data_fim):
    print(data_inicio)
    print(data_fim)
    
    relatorio = GeradorRelatorio(tipo=tipo, inicio=data_inicio, fim=data_fim) #GeradorRelatorio(tipo, inicio, fim)
    #                 tipo é um boolean (0 para Partidas e 1 para Chegadas)
    #                 inicio e fim sao datetimes na forma AAAA/MM/DD-HH:MM:SS 
    #                 (Utilizar a seguinte parte da documentação: https://docs.djangoproject.com/en/4.1/ref/forms/fields/#datetimefield )
    
    arquivo = relatorio.gera_pdf() #funcao que gera pdf a paritr do objeto instanciado acima da classe
    return FileResponse(open(arquivo,'rb'))

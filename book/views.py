from urllib.parse import urlencode, unquote
from django.shortcuts import redirect, render
from django.contrib import messages
from django.http import FileResponse
from django.shortcuts import render
from book.class_GeradorRelatorio import GeradorRelatorio
from book.forms import Codigo_Voo_Monitora, DateTimeField_ERelatorio, Formulario_Atualiza_Basico_Voos, Formulario_Cadastro_Voo, Formulario_Atualiza_Voos
from book.models import Voo
from book.enum_Status import enum_Status
from django.http.response import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth import login as login_django

# Create your views here.

def login(request):
    if request.method == 'GET':
        usuario_check = User.objects.filter(username="Cara_Crud").exists()
        if usuario_check == False:
                user_criar = "Cara_Crud"
                senha_criar= "1234"
                user_criar = User.objects.create_user(username=user_criar, password=senha_criar)
                user_criar.save()
        usuario_check = User.objects.filter(username="Cara_Relatorio").exists()
        if usuario_check == False:
                user_criar = "Cara_Relatorio"
                senha_criar= "1234"
                user_criar = User.objects.create_user(username=user_criar, password=senha_criar)
                user_criar.save()
        usuario_check = User.objects.filter(username="Torre").exists()
        if usuario_check == False:
                user_criar = "Torre"
                senha_criar= "1234"
                user_criar = User.objects.create_user(username=user_criar, password=senha_criar)
                user_criar.save()
        usuario_check = User.objects.filter(username="Funcionário").exists()
        if usuario_check == False:
                user_criar = "Funcionário"
                senha_criar= "1234"
                user_criar = User.objects.create_user(username=user_criar, password=senha_criar)
                user_criar.save()
        usuario_check = User.objects.filter(username="Companhia").exists()
        if usuario_check == False:
                user_criar = "Companhia"
                senha_criar= "1234"
                user_criar = User.objects.create_user(username=user_criar, password=senha_criar)
                user_criar.save()
        usuario_check = User.objects.filter(username="Gerente_Testes").exists()
        if usuario_check == False:
                user_criar = "Gerente_Testes"
                senha_criar= "1234"
                user_criar = User.objects.create_user(username=user_criar, password=senha_criar)
                user_criar.save()
        usuario_check = User.objects.filter(username="Piloto").exists()
        if usuario_check == False:
                user_criar = "Piloto"
                senha_criar= "1234"
                user_criar = User.objects.create_user(username=user_criar, password=senha_criar)
                user_criar.save()
        return render(request, "login.html")

    else:
        if "load_count" in request.session:
            count = request.session["load_count"] + 1
        else:
            count = 1

        request.session["load_count"] = count
        usuario = request.POST.get('login')
        senha = request.POST.get('senha')
        print(usuario)
        print(senha)
        user = authenticate(username=usuario, password=senha)
        if user:
            login_django(request, user)
            request.session["logged_user"]=usuario
            return redirect("../../inicial")
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

def logout(request):
    request.session["logged_user"]=""
    return render(request,"login.html")

def inicial(request):
    usuario = request.session["logged_user"]
    print('Logado como ' + usuario)
    context = {'usuario':usuario}
    return render(request, "inicial.html",context)

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
            companhia = form.cleaned_data['companhia_aerea']
            destino = form.cleaned_data['destino_do_voo']
            origem = form.cleaned_data['origem_do_voo'] 
            partida_prev = form.cleaned_data['partida_prevista'] 
            chegada_prev = form.cleaned_data['chegada_prevista'] 
            if (partida_prev > chegada_prev):  ## If não permite que voo possua chegada anterior a destino
                messages.success(request, 'Não é possível cadastrar um voo com chegada anterior a partida')
                context = {
                    'form' : form
                 }
                return render(request, "cadastroVoos.html", context)
            print('DESTINO: ' + str(destino))
            Voo.objects.create(
            codigo_de_voo=codigo,
            companhia_aerea = companhia,
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
        # retornaRelatorioPDF(request,tipo_relatorio,data_inicio,data_fim)
        params={
            'data_inicio':data_inicio,
            'data_fim':data_fim,
            'tipo_relatorio':tipo_relatorio
        }
        params=urlencode(params)
        # return render(request, "relatorios.html",context)
        return redirect(f"download/relatorio?{params}")


def monitoraCadastro(request):
    context = getVoosDict(None)
    return render(request,"monitoraCadastro.html",context)

def getVoosDict(form):
    todos_voos = Voo.objects.filter(status__range=[1,8]).values()
    todos_voos=associaStatus(voos=todos_voos)
    if form is not None:
        context = {
            'form' : form,
            'voos':todos_voos
        }
    else:
        context = {
            'voos':todos_voos
        }
    return context


def escolheVooMonitorado(request):
    # Receptor dos dados usados em `monitoraVoos()`
    if request.method == "GET":
        form = Codigo_Voo_Monitora()
        context = getVoosDict(form)
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
            'companhia_mostrada' : mostra_companhia(codigo_voo),
            'status_mostrado': mostra_status_do_voo(codigo_voo),
            'destino_mostrado': mostra_aeroporto_destino(codigo_voo),
            'partida_mostrada': mostra_aeroporto_partida(codigo_voo),
            'partida_prevista' : mostra_partida_prevista(codigo_voo),
            'partida_real' : mostra_partida_real(codigo_voo) if  "None" not in mostra_partida_real(codigo_voo) else "Não há partida real ainda",
            'chegada_prevista' : mostra_chegada_prevista(codigo_voo),
            'chegada_real' : mostra_chegada_real(codigo_voo) if "None" not in  mostra_chegada_real(codigo_voo) else "Não há chegada real ainda",
            'form' : form
        }
        return render(request, "monitoraVoos.html", context)
    
    else:
        form = Codigo_Voo_Monitora(request.POST)
        print(type(form))
        if form.is_valid():
            print (form.cleaned_data)
            
            codigo = form.cleaned_data['codigo_voo']
            verifica_codigo = Voo.objects.filter(codigo_de_voo=codigo).exists()
            print(verifica_codigo)
            if verifica_codigo:                 ##IF que deleta se código está na basa de dados
                voo = Voo.objects.get(codigo_de_voo=codigo)
                if int(voo.status) != 6:
                    deleta_voo(codigo)
                    messages.success(request, 'Voo deletado com sucesso.')
                    context = {
                        'form' : form
                    }
                    return render(request, "monitoraVoos.html", context)
                else:
                    messages.success(request, 'Não é possível deletar um voo em andamento.')
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
        else:
            return render(request, "monitoraVoos.html")

def deleta_voo(codigo_voo):
    voo =  Voo.objects.get(codigo_de_voo=codigo_voo)
    voo.delete()
    return

def mostra_codigo_do_voo(codigo_voo):
    voo = Voo.objects.get(codigo_de_voo=codigo_voo)
    print('Código do voo: '+ str(voo.codigo_de_voo))
    return ('Código do voo: '+ str(voo.codigo_de_voo))

def mostra_companhia(codigo_voo):
    voo = Voo.objects.get(codigo_de_voo=codigo_voo)
    print('Companhia Aérea: '+ str(voo.companhia_aerea))
    return ('Companhia Aérea: '+ str(voo.companhia_aerea))

def mostra_status_do_voo(codigo_voo):
    voo = Voo.objects.get(codigo_de_voo=codigo_voo)
    status = associaStatus(status=str(voo.status))
    print('Status do voo: '+ status)
    return ('Status do voo: '+ status)

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
    path=request.get_full_path()
    coiso=path.split('?')
    unquoted = unquote(coiso[1]) 
    print(unquote(coiso[1]))
    data_inicio,data_fim,tipo = unquoted.split('&')
    data_fim = data_fim.split('+')
    data_inicio = data_inicio.split('+')
    print('VERIFICA SPLIT: ' + str(data_fim))
    dia_inicio = data_inicio[0].split('=')[1]
    dia_fim = data_fim[0].split('=')[1]
    data_inicio = dia_inicio+ ' ' + data_inicio[1]
    data_fim = dia_fim+ ' ' + data_fim[1]
    d_fim = data_fim
    d_inicio = data_inicio
    if(d_inicio > d_fim):
        messages.success(request, 'Data inicial maior que a final')
        return render(request, "relatorios.html")
        # relatorios(request)
    else:
        print(data_fim)
        relatorio = GeradorRelatorio(tipo=tipo, inicio=data_inicio, fim=data_fim) #GeradorRelatorio(tipo, inicio, fim)
        #                 tipo é um boolean (0 para Partidas e 1 para Chegadas)
        #                 inicio e fim sao datetimes na forma AAAA/MM/DD-HH:MM:SS 
        #                 (Utilizar a seguinte parte da documentação: https://docs.djangoproject.com/en/4.1/ref/forms/fields/#datetimefield )
        if relatorio.valida():
            arquivo = relatorio.gera_pdf() #funcao que gera pdf a paritr do objeto instanciado acima da classe
            return FileResponse(open(arquivo,'rb'))
        else:
            messages.success(request, 'Não há voos com os parâmetros solicitados')
            return render(request, "relatorios.html")

def deletaCadastro(request):
    if request.method == "GET":
        form = Codigo_Voo_Monitora()

        context = {
                    'form' : form
                    }
        return render(request,"deletaCadastro.html",context)
    else:
        form = Codigo_Voo_Monitora(request.POST)
        print(type(form))
        if form.is_valid():
            print (form.cleaned_data)
            codigo = form.cleaned_data['codigo_voo']
            verifica_codigo = Voo.objects.filter(codigo_de_voo=codigo).exists()
            print(verifica_codigo)
            if verifica_codigo:
                voo = Voo.objects.get(codigo_de_voo=codigo)
                if int(voo.status) != 6:                ##IF que deleta se código está na basa de dados
                    deleta_voo(codigo)
                    messages.success(request, 'Voo deletado com sucesso.')
                    context = {
                        'form' : form
                        }
                    return render(request, "deletaCadastro.html", context)
                else:
                    messages.success(request, 'Não é possível deletar um voo em andamento.')
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
                return render(request, "deletaCadastro.html", context)
        else:
            return render(request,"deletaCadastro.html")

def atualizaBasico(request):
    if request.method == "GET":
        form = Formulario_Atualiza_Basico_Voos()
        context = {
            'form' : form
        }
        return render(request, "atualizaVoos.html", context)
        
    else:
        form = Formulario_Atualiza_Basico_Voos(request.POST)
        if form.is_valid():
            print (form.cleaned_data)
            codigo = form.cleaned_data['código_do_voo']
            verifica_codigo = Voo.objects.filter(codigo_de_voo=codigo).first()
           
            if verifica_codigo is None:                 ##IF que nao deixa criar dois voos com mesmo código
                messages.success(request, 'Não existe voo para ser atualizado')
                context = {
                    'form' : form
                 }
                return render(request, "atualizaVoos.html", context)
            voo = Voo.objects.get(codigo_de_voo=codigo)
            destino = form.cleaned_data['destino_do_voo']
            origem = form.cleaned_data['origem_do_voo'] 
            partida_prev = form.cleaned_data['partida_prevista'] 
            chegada_prev = form.cleaned_data['chegada_prevista']
            if (destino is not ''):
                voo.aeroporto_destino = destino
                voo.save()
            if (origem is not ''):
                voo.aeroporto_partida = origem
                voo.save()
            ### Partida e Chegada Previstas
            if (partida_prev and chegada_prev is not None):
                if (partida_prev > chegada_prev):  ## If não permite que voo possua chegada anterior a destino
                    messages.success(request, 'Não é possível cadastrar um voo com chegada anterior a partida')
                    context = {
                        'form' : form
                    }
                    return render(request, "atualizaVoos.html", context)
                voo.partida_prevista = partida_prev
                voo.chegada_prevista = chegada_prev
                voo.save()
            if (partida_prev is not None and chegada_prev is None):
                if (partida_prev > voo.chegada_prevista):
                    messages.success(request, 'Não é possível cadastrar um voo com chegada anterior a partida')
                    context = {
                        'form' : form
                    }
                    return render(request, "atualizaVoos.html", context)
                voo.partida_prevista = partida_prev
                voo.save()
            if (chegada_prev is not None and partida_prev is None):
                if (voo.partida_prevista > chegada_prev):
                    messages.success(request, 'Não é possível cadastrar um voo com chegada anterior a partida')
                    context = {
                        'form' : form
                    }
                    return render(request, "atualizaVoos.html", context)
                voo.chegada_prevista= chegada_prev
                voo.save()
    return render(request,"atualizaBasico.html",context)

def atualizaVoos(request):
    if request.method == "GET":
        form = Formulario_Atualiza_Voos()
        context = {
            'form' : form
        }
        return render(request, "atualizaVoos.html", context)
        
    else:
        form = Formulario_Atualiza_Voos(request.POST)
        if form.is_valid():
            print (form.cleaned_data)
            codigo = form.cleaned_data['código_do_voo']
            verifica_codigo = Voo.objects.filter(codigo_de_voo=codigo).first()
           
            if verifica_codigo is None:                 ##IF que nao deixa criar dois voos com mesmo código
                messages.success(request, 'Não existe voo para ser atualizado')
                context = {
                    'form' : form
                 }
                return render(request, "atualizaVoos.html", context)
            voo = Voo.objects.get(codigo_de_voo=codigo)
            destino = form.cleaned_data['destino_do_voo']
            origem = form.cleaned_data['origem_do_voo'] 
            companhia_aerea = form.cleaned_data['companhia_aerea']
            partida_prev = form.cleaned_data['partida_prevista'] 
            chegada_prev = form.cleaned_data['chegada_prevista'] 
            partida_r = form.cleaned_data['partida_real'] 
            chegada_r = form.cleaned_data['chegada_real']
            status = int(form.cleaned_data['status'])
            
            if status != 1:
                print("Status a cadastrar: " + str(status))
                if voo.status < status and status - voo.status == 1:
                    voo.status = status
                    voo.save()
                else:
                    messages.success(request, 'Não é possível pular um status!') 
                    context = {
                        'form' : form
                    }
                if voo.status == status:
                    messages.success(request, 'Voo está com este status') 
                    context = {
                        'form' : form
                    }
                    return render(request, "atualizaVoos.html", context)
                elif voo.status > status:
                    messages.success(request, 'Não é possível retornar a um status anterior ao atual') 
                    context = {
                        'form' : form
                    }
                    return render(request, "atualizaVoos.html", context)
            if (companhia_aerea is not ''):
                voo.companhia_aerea = companhia_aerea
                voo.save()
            if (destino is not ''):
                voo.aeroporto_destino = destino
                voo.save()
            if (origem is not ''):
                voo.aeroporto_partida = origem
                voo.save()
            ### Partida e Chegada Previstas
            if (partida_prev and chegada_prev is not None):
                if (partida_prev > chegada_prev):  ## If não permite que voo possua chegada anterior a destino
                    messages.success(request, 'Não é possível cadastrar um voo com chegada anterior a partida')
                    context = {
                        'form' : form
                    }
                    return render(request, "atualizaVoos.html", context)
                voo.partida_prevista = partida_prev
                voo.chegada_prevista = chegada_prev
                voo.save()
            if (partida_prev is not None and chegada_prev is None):
                if (partida_prev > voo.chegada_prevista):
                    messages.success(request, 'Não é possível cadastrar um voo com chegada anterior a partida')
                    context = {
                        'form' : form
                    }
                    return render(request, "atualizaVoos.html", context)
                voo.partida_prevista = partida_prev
                voo.save()
            if (chegada_prev is not None and partida_prev is None):
                if (voo.partida_prevista > chegada_prev):
                    messages.success(request, 'Não é possível cadastrar um voo com chegada anterior a partida')
                    context = {
                        'form' : form
                    }
                    return render(request, "atualizaVoos.html", context)
                voo.chegada_prevista= chegada_prev
                voo.save()


            
            
### Partida e Chegada Real

            if (partida_r is not None):
                if (voo.status == 6):
                    if (partida_r > voo.partida_prevista): 
                        messages.success(request, 'Atualizado com sucesso')
                        voo.partida_real = partida_r
                        voo.save()
                        context = {
                            'form' : form
                        }
                        return render(request, "atualizaVoos.html", context)
                    else:  # Não permite que voo decole antes do previsto
                        messages.success(request, 'Não é permitido decolar antes do previsto')
                        context = {
                            'form' : form
                        }
                        return render(request, "atualizaVoos.html", context)
                else: # Voo no status errado
                    messages.success(request, 'Não é possível cadastrar partida real para um voo não decolado')
                    context = {
                        'form' : form
                    }
                    return render(request, "atualizaVoos.html", context)  

            if (chegada_r is not None):
                if (voo.status == 7):
                    if (chegada_r > voo.chegada_prevista): 
                        messages.success(request, 'Atualizado com sucesso')
                        voo.chegada_real = chegada_r
                        voo.save()
                        context = {
                            'form' : form
                        }
                        return render(request, "atualizaVoos.html", context)
                    else:  # Não permite que voo aterrisse antes do previsto
                        messages.success(request, 'Não é permitido aterrissar antes do previsto')
                        context = {
                            'form' : form
                        }
                        return render(request, "atualizaVoos.html", context)
                else: # Voo no status errado
                    messages.success(request, 'Não é possível cadastrar chegada real para um voo não aterrissado')
                    context = {
                        'form' : form
                    }
                    return render(request, "atualizaVoos.html", context)


            # if (voo.status == 7 and voo.partida_real is not None):
            #     if (chegada_r < voo.chegada_prevista):
            #         messages.success(request, 'Não é possível cadastrar uma chegada real que não chegou ou não partiu')
            #         context = {
            #         'form' : form
            #         }
            #         return render(request, "atualizaVoos.html", context)
            #     else:
            #         voo.chegada_real = chegada_r
            #         voo.save()
            #         return render(request, "atualizaVoos.html", context)

            
            # if (partida_r is not None and chegada_r is None):
            #     if (voo.chegada_real is not None):
            #         if (partida_r > voo.chegada_real):
            #             messages.success(request, 'Não é possível cadastrar um voo com chegada anterior a partida')
            #             context = {
            #             'form' : form
            #             }
            #             return render(request, "atualizaVoos.html", context)
            #     voo.partida_real = partida_r
            #     voo.save()

            # if (chegada_r is not None and partida_r is None):
            #     if (voo.partida_real is not None):
            #         if (voo.partida_real > chegada_r):
            #             messages.success(request, 'Não é possível cadastrar um voo com chegada anterior a partida')
            #             context = {
            #                 'form' : form
            #             }   
            #             return render(request, "atualizaVoos.html", context)
            #     voo.chegada_real = chegada_r
            #     voo.save()

            

                #Refresh
                #Error msg
           # messages.success(request, 'Atualizações alteradas com sucesso.')
            context = {
                'form' : form
            }
            return render(request, "atualizaVoos.html", context)

def associaStatus(voos=None,status=None):
    if voos is not None:
        for voo in voos:
                aux = str(enum_Status(voo['status']))
                if('_' in aux):
                    aux=aux.replace('_',' ')
                print(aux[12:])
                voo['status']=aux[12:]
        return voos 
    elif status is not None:
        aux = str(enum_Status(int(status)))
        if('_' in aux):
            aux=aux.replace('_',' ')
        aux=aux[12:]
        print(aux)
        return aux

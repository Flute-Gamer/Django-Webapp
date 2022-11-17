from django.db import models
import datetime
# Create your models here.

class Voo(models.Model):
    codigo_de_voo = models.IntegerField(primary_key=True)
    status = models.IntegerField()
    aeroporto_destino = models.CharField(max_length=200, null=False)
    aeroporto_partida = models.CharField(max_length=200, null=False)
    partida_prevista = models.DateTimeField()
    partida_real = models.DateTimeField(null = True)
    chegada_prevista = models.DateTimeField()
    chegada_real = models.DateTimeField(null = True)
    class Meta:
        db_table = 'voo'

class Operador(models.Model): ##trabalha na torre
    nome = models.CharField(max_length=200, null=False)
    cpf = models.CharField(max_length=11, null=False, primary_key = True)
    email = models.CharField(max_length=200, null=False)
    class Meta:
        db_table = 'operador'

class Funcionario(models.Model): ##cara da companhia
    nome = models.CharField(max_length=200, null=False)
    cpf = models.CharField(max_length=11, null=False, primary_key = True)
    email = models.CharField(max_length=200, null=False)
    salario = models.IntegerField(null = False)
    endereco = models.CharField(max_length=200, null=False)
    senha = models.CharField(max_length=40, null=False)
    tentativas_login = models.CharField(max_length=4,null=False)
    class Meta:
        db_table = 'funcionario'

class Piloto(models.Model):
    nome = models.CharField(max_length=200, null=False)
    cpf = models.CharField(max_length=11, null=False, primary_key = True)
    email = models.CharField(max_length=200, null=False)
    salario = models.IntegerField(null = False)
    endereco = models.CharField(max_length=200, null=False)
    class Meta:
        db_table = 'piloto'

class Status(models.Model):
    status_atual = models.IntegerField(null = False, primary_key = True)
    proximo_status =  models.IntegerField()
    horario = models.DateTimeField()
    class Meta:
        db_table = 'status'

class Companhia(models.Model):
    nome = models.CharField(max_length=200, null=False)
    funcionarios = models.ForeignKey(Funcionario,on_delete=models.CASCADE)
    pilotos = models.ForeignKey(Piloto,on_delete=models.CASCADE)
    voo = models.ForeignKey(Voo,on_delete=models.CASCADE)
    id_companhia_aerea = models.IntegerField(primary_key=True)
    class Meta:
        db_table = 'companhia'

        
##Tabela Data está excluida, visto que models.DateTime já gerencia o fuso
##Criada a classe companhia aerea

from django.db import models
import datetime
# Create your models here.

class Voo(models.Model):
    codigo_de_voo = models.IntegerField(primary_key=True)
    companhia_aerea = models.CharField(max_length=200, null=False)
    status = models.IntegerField()
    aeroporto_destino = models.CharField(max_length=200, null=False)
    aeroporto_partida = models.CharField(max_length=200, null=False)
    partida_prevista = models.DateTimeField()
    partida_real = models.DateTimeField(null = True)
    chegada_prevista = models.DateTimeField()
    chegada_real = models.DateTimeField(null = True)
    class Meta:
        db_table = 'voo'

class Operador(models.Model):
    nome = models.CharField(max_length=200, null=False)
    cpf = models.CharField(max_length=11, null=False, primary_key = True)
    email = models.IntegerField(max_length=200, null=False)
    class Meta:
        db_table = 'operador'

class Funcionario(models.Model):
    nome = models.CharField(max_length=200, null=False)
    cpf = models.CharField(max_length=11, null=False, primary_key = True)
    email = models.IntegerField(max_length=200, null=False)
    salario = models.IntegerField(null = False)
    endereco = models.IntegerField(max_length=200, null=False)
    companhia_aerea = models.CharField(max_length=200, null=False)
    class Meta:
        db_table = 'funcionario'

class Piloto(models.Model):
    nome = models.CharField(max_length=200, null=False)
    cpf = models.CharField(max_length=11, null=False, primary_key = True)
    email = models.IntegerField(max_length=200, null=False)
    salario = models.IntegerField(null = False)
    endereco = models.IntegerField(max_length=200, null=False)
    companhia_aerea = models.CharField(max_length=200, null=False)
    class Meta:
        db_table = 'piloto'

class Status(models.Model):
    status_atual = models.IntegerField(null = False, primary_key = True)
    proximo_status =  models.IntegerField()
    horario = models.DateTimeField()
    class Meta:
        db_table = 'status'

##Tabela Data está excluida, visto que models.DateTime já gerencia o fuso
##Na primeira imagem na tabela Voo, faltou aeropoto_partida

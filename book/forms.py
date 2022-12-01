from django import forms

## Classe de formulários
class Formulario_Cadastro_Voo(forms.Form):
    código_do_voo = forms.IntegerField(min_value=0)
    destino_do_voo = forms.CharField()
    origem_do_voo = forms.CharField()
    companhia_aerea = forms.CharField()
    partida_prevista = forms.DateTimeField(error_messages={'invalid': "Esta data é inválida!"})
    chegada_prevista = forms.DateTimeField(error_messages={'invalid': "Esta data é inválida!"})

class Formulario_Atualiza_Voos(forms.Form):
    CHOICES = (
        (1,'Embarcando'),
        (2,'Programado'),
        (3,'Taxiando'),
        (4,'Pronto'),
        (5,'Autorizado'),
        (6,'Em voo'),
        (7,'Aterrisado'),
        (8,'Cancelado'),
        (9,'Arquivado')
    )
    código_do_voo = forms.IntegerField(min_value=0)
    companhia_aerea = forms.CharField()
    destino_do_voo = forms.CharField(required = False)
    origem_do_voo = forms.CharField(required = False)
    partida_prevista = forms.DateTimeField(error_messages={'invalid': "Esta data é inválida!"}, required = False)
    chegada_prevista = forms.DateTimeField(error_messages={'invalid': "Esta data é inválida!"}, required = False)
    partida_real = forms.DateTimeField(error_messages={'invalid': "Esta data é inválida!"}, required = False)
    chegada_real = forms.DateTimeField(error_messages={'invalid': "Esta data é inválida!"}, required = False)
    status = forms.CharField(widget=forms.Select(choices=CHOICES))

class Formulario_Atualiza_Basico_Voos(forms.Form):
    código_do_voo = forms.IntegerField(min_value=0)
    companhia_aerea = forms.CharField()
    destino_do_voo = forms.CharField(required = False)
    origem_do_voo = forms.CharField(required = False)
    partida_prevista = forms.DateTimeField(error_messages={'invalid': "Esta data é inválida!"}, required = False)
    chegada_prevista = forms.DateTimeField(error_messages={'invalid': "Esta data é inválida!"}, required = False)

class Codigo_Voo_Monitora(forms.Form):
    codigo_voo = forms.IntegerField(min_value=0,required=False)


class DateTimeField_ERelatorio(forms.Form):
    CHOICES=[('partida','Relatório de Partida'),
         ('chegada','Relatório de Chegada')]
    tipo = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    data_inicio = forms.DateTimeField(error_messages={'invalid': "Esta data é inválida!"})
    data_fim = forms.DateTimeField(error_messages={'invalid': "Esta data é inválida!"})

from django import forms

## Classe de formulários
class Formulario_Cadastro_Voo(forms.Form):
    código_do_voo = forms.IntegerField(min_value=0)
    destino_do_voo = forms.CharField()
    origem_do_voo = forms.CharField()
    partida_prevista = forms.DateField(error_messages={'invalid': "Esta data é inválida!"})
    chegada_prevista = forms.DateField(error_messages={'invalid': "Esta data é inválida!"})

class Codigo_Voo_Monitora(forms.Form):
    codigo_voo = forms.IntegerField(min_value=0)

class DateTimeField_ERelatorio(forms.Form):
    data_inicio = forms.DateTimeField(error_messages={'invalid': "Esta data é inválida!"})
    data_fim = forms.DateTimeField(error_messages={'invalid': "Esta data é inválida!"})

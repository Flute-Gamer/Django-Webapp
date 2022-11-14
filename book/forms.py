from django import forms
from book.class_voo import Voo

## Classe de formulários
class Formulario_Cadastro_Voo(forms.Form):
    código_do_voo = forms.IntegerField()
    destino_do_voo = forms.CharField()
    origem_do_voo = forms.CharField()
    partida_prevista = forms.DateField(error_messages={'invalid': "Esta data é inválida!"})
    chegada_prevista = forms.DateField(error_messages={'invalid': "Esta data é inválida!"})

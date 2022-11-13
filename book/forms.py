from django import forms
from book.class_voo import Voo


class Formulario_Cadastro_Voo(forms.Form):
    destino_do_voo = forms.CharField()
    origem_do_voo = forms.CharField()
    partida_prevista = forms.DateField()
    chegada_prevista = forms.DateField()

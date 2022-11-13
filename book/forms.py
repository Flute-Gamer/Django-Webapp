from django import forms
from book.class_voo import Voo

class DateInput(forms.DateInput):
    inpute_type = 'date'

class TextInput(forms.TextInput):
    input_type: str = 'text'

class Form(forms.Form):
    destino_voo = forms.TextInput(widget = TextInput)
    origem_voo = forms.TextInput(widget = TextInput)
    partida_prevista = forms.DateField(widget = DateInput)
    chegada_prevista = forms.DateField(widget = DateInput)

class ModelForm(forms.Form):
    class Meta:
        widgets = {'destino_voo' : TextInput(),
                   'origem_voo'  : TextInput(),
                   'partida_prevista' : DateInput(), 
                   'chegada_prevista' : DateInput()}
        voo = Voo(0, 'destino_voo', 'origem_voo', 'partida_prevista', 'chegada_prevista')
        print (voo.aeroporto_destino, voo.aeroporto_partida, voo.chegada_prevista)
        
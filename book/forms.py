from django import forms

class DateInput(forms.DateInput):
    inpute_type = 'date'

class Example_Form(forms.Form)
    my_date_field = forms.DateField(widget = DateInput)

class ExampleModelForm(forms.Form):
    class Meta:
        widgets = {'my_date_field' : DateInput()}
from django import forms
from .models import Menu, Cliente

class JugadorForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ('nombre', 'anio','personajes')

class PForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('nombre', 'anio')

def __init__(self, *args, **kwargs):
    super(JugadorForm, self).__init__(*args, **kwargs)
    self.fields["personajes"].widget = forms.widgets.CheckboxSelectMultiple()
    self.fields["personajes"].help_text = "Ingrese los personajes de este jugador"
    self.fields["personajes"].queryset = Personaje.objects.all()

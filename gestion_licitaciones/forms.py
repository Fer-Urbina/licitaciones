from django import forms
from django.forms import inlineformset_factory
from .models import Licitacion, DetalleLicitacion, ComponenteTecnico

class LicitacionForm(forms.ModelForm):
    class Meta:
        model = Licitacion
        fields = ['titulo', 'descripcion', 'fecha_cierre']

class DetalleLicitacionForm(forms.ModelForm):
    class Meta:
        model = DetalleLicitacion
        fields = ['nombre', 'cantidad']

class ComponenteTecnicoForm(forms.ModelForm):
    class Meta:
        model = ComponenteTecnico
        fields = ['especificacion']

ComponenteTecnicoFormSet = inlineformset_factory(
    DetalleLicitacion, 
    ComponenteTecnico, 
    form=ComponenteTecnicoForm, 
    extra=1, 
    can_delete=True
)
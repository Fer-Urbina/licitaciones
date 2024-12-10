from django import forms
from .models import Licitacion

class LicitacionForm(forms.ModelForm):
    class Meta:
        model = Licitacion
        fields = ['titulo', 'descripcion', 'fecha_cierre']
        labels = {
            'titulo': 'Título de la Licitación',
            'descripcion': 'Descripción',
            'fecha_cierre': 'Fecha de Cierre',
        }
        widgets = {
            'fecha_cierre': forms.DateInput(attrs={'type': 'date'}),
        }
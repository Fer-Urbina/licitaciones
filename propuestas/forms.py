from django import forms
from .models import Propuesta

class PropuestaForm(forms.ModelForm):
    class Meta:
        model = Propuesta
        fields = ['oferta_tecnica', 'oferta_economica']
        labels = {
            'oferta_tecnica': 'Oferta Técnica',
            'oferta_economica': 'Oferta Económica',
        }
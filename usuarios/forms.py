from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario

class RegistroUsuarioForm(UserCreationForm):
    email = forms.EmailField(label='Correo Electrónico', max_length=255, required=True)

    class Meta:
        model = Usuario
        fields = ['username', 'email', 'password1', 'password2', 'es_licitador']
        labels = {
            'username': 'Nombre de Usuario',
            'es_licitador': '¿Es Licitador?',
        }
        help_texts = {
            'username': 'Elige un nombre de usuario único.',
            'password1': 'Tu contraseña debe tener al menos 8 caracteres y no ser totalmente numérica.',
        }
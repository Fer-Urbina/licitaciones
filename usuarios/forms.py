from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario

class RegistroUsuarioForm(UserCreationForm):
    email = forms.EmailField(
        label='Correo Electrónico',
        max_length=255,
        required=True,
        help_text='Introduce una dirección de correo válida.'
    )
    first_name = forms.CharField(
        label='Nombre',
        max_length=50,
        required=True,
        help_text='Introduce tu nombre.'
    )
    last_name = forms.CharField(
        label='Apellido',
        max_length=50,
        required=True,
        help_text='Introduce tu apellido.'
    )

    class Meta:
        model = Usuario
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name', 'es_licitador']
        labels = {
            'username': 'Nombre de Usuario',
            'email': 'Correo Electrónico',
            'password1': 'Contraseña',
            'password2': 'Confirmar Contraseña',
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'es_licitador': '¿Es Licitador?',
        }
        help_texts = {
            'username': 'Elige un nombre de usuario único.',
            'password1': 'Tu contraseña debe tener al menos 8 caracteres y no ser totalmente numérica.',
            'password2': 'Introduce nuevamente la misma contraseña para confirmar.',
        }

    def save(self, commit=True):
        """
        Sobrescribe el método save para garantizar que los datos adicionales (first_name, last_name)
        se guarden correctamente en el modelo Usuario.
        """
        usuario = super().save(commit=False)
        usuario.first_name = self.cleaned_data.get('first_name')
        usuario.last_name = self.cleaned_data.get('last_name')
        if commit:
            usuario.save()
        return usuario
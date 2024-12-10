from django.db import models
from usuarios.models import Usuario

class Licitacion(models.Model):
    ESTADO_CHOICES = [
        ('Abierta', 'Abierta'),
        ('Cerrada', 'Cerrada'),
    ]
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    fecha_cierre = models.DateTimeField()
    estado = models.CharField(
        max_length=10,
        choices=ESTADO_CHOICES,
        default='Abierta',
        help_text="Define si la licitación está abierta o cerrada"
    )
    usuario = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE,
        related_name='licitaciones',
        help_text="Usuario que creó la licitación"
    )
    ganador = models.OneToOneField(
        'propuestas.Propuesta',  # Referencia diferida como cadena
        null=True,  # Puede ser null porque inicialmente no hay un ganador.
        blank=True,  # Permitir que el campo quede vacío.
        on_delete=models.SET_NULL,  # Si se elimina la propuesta, el campo se establece como null.
        related_name="ganador_de",  # Nombre de la relación inversa para acceder desde Propuesta.
    )

    def __str__(self):
        return self.titulo
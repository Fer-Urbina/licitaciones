from django.db import models
from django.utils import timezone
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
    )
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='licitaciones')

    def __str__(self):
        return self.titulo


class DetalleLicitacion(models.Model):
    licitacion = models.ForeignKey(Licitacion, on_delete=models.CASCADE, related_name='detalles')
    nombre = models.CharField(max_length=255, help_text="Nombre del equipo, por ejemplo, CPU, Monitor.")
    cantidad = models.PositiveIntegerField(default=1, help_text="Cantidad requerida.")

    def __str__(self):
        return f"{self.nombre} - {self.licitacion.titulo}"


class ComponenteTecnico(models.Model):
    detalle = models.ForeignKey(DetalleLicitacion, on_delete=models.CASCADE, related_name='componentes')
    especificacion = models.CharField(max_length=255, help_text="Especificación técnica, por ejemplo, 'Procesador Intel Core i7'.")

    def __str__(self):
        return self.especificacion
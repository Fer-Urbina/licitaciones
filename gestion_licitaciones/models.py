from django.db import models
from usuarios.models import Usuario

class Licitacion(models.Model):
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    fecha_cierre = models.DateTimeField()
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='licitaciones')

    def __str__(self):
        return self.titulo
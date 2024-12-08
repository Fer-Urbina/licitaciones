from django.db import models
from propuestas.models import Propuesta
from usuarios.models import Usuario

class Evaluacion(models.Model):
    propuesta = models.ForeignKey(Propuesta, on_delete=models.CASCADE, related_name='evaluaciones')
    evaluador = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='evaluaciones_realizadas')
    puntuacion = models.IntegerField()
    comentarios = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Evaluación de {self.propuesta} por {self.evaluador.username}"
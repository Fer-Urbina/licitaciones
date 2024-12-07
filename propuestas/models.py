from django.db import models
from gestion_licitaciones.models import Licitacion
from usuarios.models import Usuario

class Propuesta(models.Model):
    licitacion = models.ForeignKey(Licitacion, on_delete=models.CASCADE, related_name="propuestas")
    proveedor = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="propuestas")
    oferta_tecnica = models.TextField()
    oferta_economica = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Propuesta de {self.proveedor.username} para {self.licitacion.titulo}"
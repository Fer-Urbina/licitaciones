from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    es_licitador = models.BooleanField(default=False)
    es_proveedor = models.BooleanField(default=False)

    def __str__(self):
        return self.username
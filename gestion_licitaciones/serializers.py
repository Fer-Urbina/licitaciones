from rest_framework import serializers
from .models import Licitacion

class LicitacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Licitacion
        fields = ['id', 'titulo', 'descripcion', 'fecha_publicacion', 'fecha_cierre', 'usuario']

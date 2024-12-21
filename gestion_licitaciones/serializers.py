from rest_framework import serializers
from .models import Licitacion, DetalleLicitacion

class DetalleLicitacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalleLicitacion
        fields = ['id', 'nombre', 'descripcion', 'cantidad']

class LicitacionSerializer(serializers.ModelSerializer):
    detalles = DetalleLicitacionSerializer(many=True)  # Permite la creación de detalles junto con la licitación

    class Meta:
        model = Licitacion
        fields = ['id', 'titulo', 'descripcion', 'fecha_publicacion', 'fecha_cierre', 'estado', 'usuario', 'detalles']

    def create(self, validated_data):
        detalles_data = validated_data.pop('detalles', [])
        licitacion = Licitacion.objects.create(**validated_data)
        for detalle_data in detalles_data:
            DetalleLicitacion.objects.create(licitacion=licitacion, **detalle_data)
        return licitacion
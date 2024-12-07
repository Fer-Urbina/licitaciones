from rest_framework import serializers
from .models import Propuesta

class PropuestaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Propuesta
        fields = ['id', 'licitacion', 'proveedor', 'oferta_tecnica', 'oferta_economica', 'fecha_creacion']
        read_only_fields = ['fecha_creacion']  # Campo solo lectura, se genera automáticamente
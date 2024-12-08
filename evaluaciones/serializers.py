from rest_framework import serializers
from .models import Evaluacion

class EvaluacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evaluacion
        fields = ['id', 'propuesta', 'evaluador', 'puntuacion', 'comentarios', 'fecha_creacion']
        read_only_fields = ['evaluador', 'fecha_creacion']
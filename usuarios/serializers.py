from rest_framework import serializers
from .models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'es_licitador', 'es_proveedor']

class RegistroSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Usuario
        fields = ['username', 'email', 'password', 'first_name', 'last_name', 'es_licitador', 'es_proveedor']

    def create(self, validated_data):
        usuario = Usuario.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
            es_licitador=validated_data.get('es_licitador', False),
            es_proveedor=validated_data.get('es_proveedor', False),
        )
        return usuario
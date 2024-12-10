from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny
from rest_framework import status
from .models import Propuesta
from gestion_licitaciones.models import Licitacion
from .serializers import PropuestaSerializer
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

class PropuestaCreateView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, licitacion_id):
        try:
            licitacion = Licitacion.objects.get(id=licitacion_id)
        except Licitacion.DoesNotExist:
            return Response({'error': 'Licitación no encontrada'}, status=status.HTTP_404_NOT_FOUND)

        if not request.user.es_proveedor:
            return Response({'error': 'Solo los proveedores pueden enviar propuestas'}, status=status.HTTP_403_FORBIDDEN)

        data = request.data
        data['licitacion'] = licitacion.id
        data['proveedor'] = request.user.id

        serializer = PropuestaSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PropuestaListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        if request.user.es_proveedor:
            propuestas = Propuesta.objects.filter(proveedor=request.user)
        else:
            return Response({'error': 'Acceso no permitido'}, status=status.HTTP_403_FORBIDDEN)

        serializer = PropuestaSerializer(propuestas, many=True)
        return Response(serializer.data)

class PropuestaListForLicitacionView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, licitacion_id):
        if not request.user.es_licitador:
            return Response({'error': 'Solo los licitadores pueden consultar las propuestas'}, status=status.HTTP_403_FORBIDDEN)

        try:
            licitacion = Licitacion.objects.get(id=licitacion_id, usuario=request.user)
        except Licitacion.DoesNotExist:
            return Response({'error': 'Licitación no encontrada o no tiene permisos para verla'}, status=status.HTTP_404_NOT_FOUND)

        propuestas = licitacion.propuestas.all()
        serializer = PropuestaSerializer(propuestas, many=True)
        return Response(serializer.data)

@login_required
def listar_propuestas_view(request):
    propuestas = Propuesta.objects.filter(proveedor=request.user)
    return render(request, 'propuestas/listar_propuestas.html', {'propuestas': propuestas})

@login_required
def listar_propuestas_por_licitacion(request, licitacion_id):
    licitacion = get_object_or_404(Licitacion, id=licitacion_id)

    if not request.user.es_licitador or licitacion.usuario != request.user:
        return render(request, 'error.html', {'message': 'No tienes permisos para ver las propuestas de esta licitación.'})

    propuestas = licitacion.propuestas.all()

    return render(request, 'propuestas/listar_propuestas_por_licitacion.html', {'licitacion': licitacion, 'propuestas': propuestas})
from rest_framework.views import APIView
from rest_framework.response import Response
from django.utils.timezone import now
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView
from .models import Licitacion
from .serializers import LicitacionSerializer
from propuestas.models import Propuesta

class LicitacionListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        licitaciones = Licitacion.objects.filter(usuario=request.user)
        serializer = LicitacionSerializer(licitaciones, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        data['usuario'] = request.user.id
        serializer = LicitacionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LicitacionDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        try:
            licitacion = Licitacion.objects.get(pk=pk, usuario=request.user)
        except Licitacion.DoesNotExist:
            return Response({'error': 'Licitacion not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = LicitacionSerializer(licitacion)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            licitacion = Licitacion.objects.get(pk=pk, usuario=request.user)
        except Licitacion.DoesNotExist:
            return Response({'error': 'Licitacion not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = LicitacionSerializer(licitacion, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            licitacion = Licitacion.objects.get(pk=pk, usuario=request.user)
        except Licitacion.DoesNotExist:
            return Response({'error': 'Licitacion not found'}, status=status.HTTP_404_NOT_FOUND)
        licitacion.delete()
        return Response({'message': 'Licitacion deleted'}, status=status.HTTP_204_NO_CONTENT)

class LicitacionListView(ListAPIView):
    queryset = Licitacion.objects.all()
    serializer_class = LicitacionSerializer

class SeleccionarGanadorView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, licitacion_id, propuesta_id):
        try:
            licitacion = Licitacion.objects.get(id=licitacion_id, usuario=request.user)
        except Licitacion.DoesNotExist:
            return Response({'error': 'No tiene permiso para gestionar esta licitación o no existe.'}, status=status.HTTP_404_NOT_FOUND)

        if licitacion.fecha_cierre <= now() or licitacion.ganador is not None:
            return Response({'error': 'No puede seleccionar un ganador para una licitación cerrada o ya gestionada.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            propuesta = Propuesta.objects.get(id=propuesta_id, licitacion=licitacion)
        except Propuesta.DoesNotExist:
            return Response({'error': 'Propuesta no encontrada en esta licitación.'}, status=status.HTTP_404_NOT_FOUND)

        licitacion.ganador = propuesta
        licitacion.save()

        return Response({
            'message': f'La propuesta con id {propuesta.id} ha sido seleccionada como ganadora para la licitación {licitacion.titulo}'
        }, status=status.HTTP_200_OK)

class LicitacionesPorEstadoView(ListAPIView):
    serializer_class = LicitacionSerializer

    def get_queryset(self):
        estado = self.kwargs['estado']
        if estado == 'abiertas':
            return Licitacion.objects.filter(fecha_cierre__gt=now(), ganador__isnull=True)
        elif estado == 'cerradas':
            return Licitacion.objects.filter(fecha_cierre__lte=now()) | Licitacion.objects.filter(ganador__isnull=False)
        else:
            return Licitacion.objects.none()
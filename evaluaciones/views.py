from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import Evaluacion
from propuestas.models import Propuesta
from .serializers import EvaluacionSerializer


class CrearEvaluacionView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, propuesta_id):
        # Verificar si el usuario es un licitador
        if not request.user.es_licitador:
            return Response({'error': 'Solo los licitadores pueden crear evaluaciones'}, status=status.HTTP_403_FORBIDDEN)

        # Verificar que la propuesta existe
        try:
            propuesta = Propuesta.objects.get(id=propuesta_id)
        except Propuesta.DoesNotExist:
            return Response({'error': 'Propuesta no encontrada'}, status=status.HTTP_404_NOT_FOUND)

        # Agregar propuesta y evaluador al serializer
        data = request.data
        data['propuesta'] = propuesta.id
        data['evaluador'] = request.user.id

        serializer = EvaluacionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ListarEvaluacionesPorPropuestaView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, propuesta_id):
        # Verificar que la propuesta existe
        try:
            propuesta = Propuesta.objects.get(id=propuesta_id)
        except Propuesta.DoesNotExist:
            return Response({'error': 'Propuesta no encontrada'}, status=status.HTTP_404_NOT_FOUND)

        # Obtener las evaluaciones para la propuesta
        evaluaciones = Evaluacion.objects.filter(propuesta=propuesta)
        serializer = EvaluacionSerializer(evaluaciones, many=True)
        return Response(serializer.data)


class ListarEvaluacionesPorLicitadorView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Verificar si el usuario es un licitador
        if not request.user.es_licitador:
            return Response({'error': 'Solo los licitadores pueden ver sus evaluaciones'}, status=status.HTTP_403_FORBIDDEN)

        # Obtener las evaluaciones realizadas por el licitador
        evaluaciones = Evaluacion.objects.filter(evaluador=request.user)
        serializer = EvaluacionSerializer(evaluaciones, many=True)
        return Response(serializer.data)
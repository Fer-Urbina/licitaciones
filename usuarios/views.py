from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Usuario
from .serializers import RegistroSerializer, UsuarioSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated

class RegistroView(APIView):
    permission_classes = [AllowAny]  # Permitir acceso sin autenticación

    def post(self, request):
        serializer = RegistroSerializer(data=request.data)
        if serializer.is_valid():
            usuario = serializer.save()
            refresh = RefreshToken.for_user(usuario)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UsuarioDetailView(APIView):
    permission_classes = [IsAuthenticated]  # Verifica que el usuario esté autenticado

    def get(self, request):
        usuario = request.user
        serializer = UsuarioSerializer(usuario)
        return Response(serializer.data)
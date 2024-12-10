from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Usuario
from .serializers import RegistroSerializer, UsuarioSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from gestion_licitaciones.models import Licitacion
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegistroUsuarioForm
from django.contrib.auth.decorators import login_required

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

def signup_view(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registro exitoso. Ahora puedes iniciar sesión.')
            return redirect('login')
        else:
            # Mostrar errores específicos
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        form = RegistroUsuarioForm()
    return render(request, 'usuarios/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('correo')
        password = request.POST.get('password')
        try:
            user = Usuario.objects.get(email=email)
            # Autenticar usando el `username` del modelo Usuario
            user = authenticate(request, username=user.username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')  # Redirigir al dashboard después de iniciar sesión
            else:
                messages.error(request, 'Credenciales incorrectas. Intenta nuevamente.')
        except Usuario.DoesNotExist:
            messages.error(request, 'No existe un usuario con ese correo.')
    return render(request, 'usuarios/login.html')

def logout_view(request):
    """
    Cierra la sesión del usuario y redirige a la página de inicio.
    """
    logout(request)
    return redirect('index')  # Redirigir a la página de inicio después del logout

@login_required
def dashboard_view(request):
    user = request.user
    if user.es_licitador:
        licitaciones = Licitacion.objects.filter(usuario=user)  # Licitaciones creadas por el usuario
        context = {'rol': 'Licitador', 'licitaciones': licitaciones}
    else:
        licitaciones_abiertas = Licitacion.objects.filter(estado='Abierta')  # Solo licitaciones abiertas
        context = {'rol': 'Proveedor', 'licitaciones_abiertas': licitaciones_abiertas}
    return render(request, 'usuarios/dashboard.html', context)
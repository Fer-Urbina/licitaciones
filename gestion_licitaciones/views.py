from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView
from rest_framework import status
from django.utils.timezone import now
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Licitacion, DetalleLicitacion
from .serializers import LicitacionSerializer
from .forms import LicitacionForm, DetalleLicitacionForm, ComponenteTecnico
from propuestas.models import Propuesta
from propuestas.forms import PropuestaForm
from django.forms import modelformset_factory
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

class LicitacionCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = LicitacionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(usuario=request.user)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

def index(request):
    return render(request, 'index.html')

def login_view(request):
    return render(request, 'login.html')

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

@login_required
def crear_licitacion_view(request):
    if request.method == 'POST':
        licitacion_form = LicitacionForm(request.POST)
        if licitacion_form.is_valid():
            licitacion = licitacion_form.save(commit=False)
            licitacion.usuario = request.user
            licitacion.save()

            # Procesar detalles de la tabla
            nombres = request.POST.getlist('nombre[]')
            cantidades = request.POST.getlist('cantidad[]')
            componentes = request.POST.getlist('componentes[]')

            for nombre, cantidad, componentes_detalle in zip(nombres, cantidades, componentes):
                detalle = DetalleLicitacion.objects.create(
                    licitacion=licitacion,
                    nombre=nombre,
                    cantidad=cantidad,
                )
                for componente in componentes_detalle.splitlines():
                    if componente.strip():
                        ComponenteTecnico.objects.create(detalle=detalle, especificacion=componente.strip())

            return redirect('dashboard')

    else:
        licitacion_form = LicitacionForm()

    return render(request, 'licitaciones/crear_licitacion.html', {
        'licitacion_form': licitacion_form,
    })

@login_required
def ver_licitacion_view(request, licitacion_id):
    licitacion = get_object_or_404(Licitacion, id=licitacion_id)
    detalles = licitacion.detalles.all()
    return render(request, 'licitaciones/ver_licitacion.html', {
        'licitacion': licitacion,
        'detalles': detalles,
    })

@login_required
def agregar_detalle_view(request, licitacion_id):
    licitacion = get_object_or_404(Licitacion, id=licitacion_id)

    if request.method == 'POST':
        form = DetalleLicitacionForm(request.POST)
        if form.is_valid():
            detalle = form.save(commit=False)
            detalle.licitacion = licitacion
            detalle.save()
            return redirect('ver_licitacion', licitacion_id=licitacion.id)
    else:
        form = DetalleLicitacionForm()

    return render(request, 'gestion_licitaciones/agregar_detalle.html', {
        'form': form,
        'licitacion': licitacion,
    })

@login_required
def enviar_propuesta_view(request, licitacion_id):
    licitacion = get_object_or_404(Licitacion, id=licitacion_id, estado='Abierta')
    if request.method == 'POST':
        form = PropuestaForm(request.POST)
        if form.is_valid():
            propuesta = form.save(commit=False)
            propuesta.licitacion = licitacion
            propuesta.proveedor = request.user
            propuesta.save()
            return HttpResponseRedirect(reverse('dashboard'))  # Redirige al dashboard
    else:
        form = PropuestaForm()
    return render(request, 'propuestas/enviar_propuesta.html', {'form': form, 'licitacion': licitacion})

@login_required
def seleccionar_ganador_view(request, licitacion_id, propuesta_id):
    licitacion = get_object_or_404(Licitacion, id=licitacion_id, usuario=request.user)

    if licitacion.estado == 'Abierta':
        return render(request, 'error.html', {'message': 'La licitación aún está abierta. No se puede seleccionar un ganador.'})

    if licitacion.ganador:
        return render(request, 'error.html', {'message': 'Ya se ha seleccionado un ganador para esta licitación.'})

    propuesta = get_object_or_404(Propuesta, id=propuesta_id, licitacion=licitacion)

    licitacion.ganador = propuesta
    licitacion.save()

    return HttpResponseRedirect(reverse('dashboard'))  # Redirige al dashboard
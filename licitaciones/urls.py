from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
from gestion_licitaciones import views as licitaciones_views  # Importar vistas de `gestion_licitaciones`

def root_view(request):
    return JsonResponse({"message": "API de licitaciones está funcionando correctamente."})

urlpatterns = [
    path('', licitaciones_views.index, name='index'),  # Vista para la raíz
    path('login/', licitaciones_views.login_view, name='login'),
    path('dashboard/', licitaciones_views.dashboard, name='dashboard'),
    path('signup/', include('usuarios.urls')),  # Incluir la vista de registro
    path('admin/', admin.site.urls),
    path('api/usuarios/', include('usuarios.urls')),
    path('api/licitaciones/', include('gestion_licitaciones.urls')),  # Conecta las rutas de licitaciones
    path('api/propuestas/', include('propuestas.urls')),  # Conecta las rutas de propuestas
    path('api/evaluaciones/', include('evaluaciones.urls')),
    path('crear/', licitaciones_views.crear_licitacion_view, name='crear_licitacion'),  # Ruta para crear licitación
    path('licitaciones/', licitaciones_views.listar_licitaciones, name='licitaciones'),  # Ruta para listar licitaciones
]
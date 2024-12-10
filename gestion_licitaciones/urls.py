from django.urls import path
from . import views
from .views import (
    LicitacionListCreateView,
    LicitacionDetailView,
    LicitacionListView,
    SeleccionarGanadorView,
    LicitacionesPorEstadoView
)

urlpatterns = [
    path('', LicitacionListCreateView.as_view(), name='licitacion-list-create'),
    path('<int:pk>/', LicitacionDetailView.as_view(), name='licitacion-detail'),
    path('all/', LicitacionListView.as_view(), name='licitacion-list'),
    path('ganador/<int:licitacion_id>/<int:propuesta_id>/', SeleccionarGanadorView.as_view(), name='seleccionar-ganador'),
    path('estado/<str:estado>/', LicitacionesPorEstadoView.as_view(), name='licitaciones-por-estado'),
    path('crear/', views.crear_licitacion_view, name='crear_licitacion'),
    path('ver/<int:licitacion_id>/', views.ver_licitacion_view, name='ver_licitacion'),
    path('propuesta/enviar/<int:licitacion_id>/', views.enviar_propuesta_view, name='enviar_propuesta'),
]
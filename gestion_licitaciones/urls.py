from django.urls import path
from .views import (
    LicitacionListCreateView,
    LicitacionDetailView,
    LicitacionListView,
    SeleccionarGanadorView,
    LicitacionesPorEstadoView,
    crear_licitacion_view,
    ver_licitacion_view,
    enviar_propuesta_view,
    seleccionar_ganador_view,
)

urlpatterns = [
    path('', LicitacionListCreateView.as_view(), name='licitacion-list-create'),
    path('<int:pk>/', LicitacionDetailView.as_view(), name='licitacion-detail'),
    path('all/', LicitacionListView.as_view(), name='licitacion-list'),
    path('ganador/<int:licitacion_id>/<int:propuesta_id>/', SeleccionarGanadorView.as_view(), name='seleccionar-ganador'),
    path('estado/<str:estado>/', LicitacionesPorEstadoView.as_view(), name='licitaciones-por-estado'),
    path('crear/', crear_licitacion_view, name='crear_licitacion'),
    path('ver/<int:licitacion_id>/', ver_licitacion_view, name='ver_licitacion'),
    path('propuesta/enviar/<int:licitacion_id>/', enviar_propuesta_view, name='enviar_propuesta'),
    path('seleccionar_ganador/<int:licitacion_id>/<int:propuesta_id>/', seleccionar_ganador_view, name='seleccionar_ganador'),
]
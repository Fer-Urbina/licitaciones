from django.urls import path
from . import views
from .views import PropuestaCreateView, PropuestaListView, PropuestaListForLicitacionView

urlpatterns = [
    path('create/<int:licitacion_id>/', PropuestaCreateView.as_view(), name='crear-propuesta'),
    path('list/', PropuestaListView.as_view(), name='listar-propuestas'),
    path('licitacion/<int:licitacion_id>/', PropuestaListForLicitacionView.as_view(), name='propuestas-licitacion'),
    path('mis_propuestas/', views.listar_propuestas_view, name='mis_propuestas'),
]
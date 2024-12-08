from django.urls import path
from .views import CrearEvaluacionView, ListarEvaluacionesPorPropuestaView, ListarEvaluacionesPorLicitadorView

urlpatterns = [
    path('create/<int:propuesta_id>/', CrearEvaluacionView.as_view(), name='crear-evaluacion'),
    path('propuesta/<int:propuesta_id>/', ListarEvaluacionesPorPropuestaView.as_view(), name='listar-evaluaciones-propuesta'),
    path('licitador/', ListarEvaluacionesPorLicitadorView.as_view(), name='listar-evaluaciones-licitador'),
]
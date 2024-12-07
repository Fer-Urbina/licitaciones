from django.urls import path
from .views import (
    LicitacionListCreateView,
    LicitacionDetailView,
    LicitacionListView
)

urlpatterns = [
    path('', LicitacionListCreateView.as_view(), name='licitacion-list-create'),
    path('<int:pk>/', LicitacionDetailView.as_view(), name='licitacion-detail'),
    path('all/', LicitacionListView.as_view(), name='licitacion-list'),
]
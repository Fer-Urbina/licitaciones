from django.urls import path
from . import views
from .views import signup_view, login_view, logout_view, RegistroView, UsuarioDetailView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('register/', RegistroView.as_view(), name='register'),  # Registro vía API
    path('signup/', signup_view, name='signup'),  # Formulario de registro (HTML)
    path('login/', login_view, name='login'),  # Formulario de login (HTML)
    path('api/login/', TokenObtainPairView.as_view(), name='api_login'),  # Login vía API (JWT)
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Refrescar token JWT
    path('me/', UsuarioDetailView.as_view(), name='me'),  # Detalles del usuario
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('logout/', logout_view, name='logout'), 
]
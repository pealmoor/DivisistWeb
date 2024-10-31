# estudiante/urls.py

from django.urls import path
from .views import estudiante_list
from .views import estudiante_detail  # Asegúrate de tener esto

urlpatterns = [
    path('', estudiante_list, name='estudiante_list'),
    path('<int:pk>/', estudiante_detail, name='estudiante-detail'),   # Lista de estudiantes
    # Agrega otras rutas si es necesario
]

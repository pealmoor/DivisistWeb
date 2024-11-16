from django.urls import path
from .views import HorarioList, HorariosPorEstudiante
from . import views

urlpatterns = [
    path('api/horarios/', HorarioList.as_view(), name='horario-list'),  # Todos los horarios
    path('api/horarios/<int:estudiante_id>/', HorariosPorEstudiante.as_view(), name='horarios-por-estudiante'), 
    path('horario/', views.horario_view, name='horario'), # Horarios de un estudiante
]
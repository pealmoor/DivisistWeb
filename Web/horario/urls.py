# horario/urls.py

from django.urls import path
from .views import horario_list
from .views import horario_detail 

urlpatterns = [
    path('', horario_list, name='horario_list'),  # Lista de horarios
    path('<int:pk>/', horario_detail, name='estudiante-detail'),
]

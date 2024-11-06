from django.urls import path
from .views import profesor_list
from .views import profesor_detail 


urlpatterns = [
    path('', profesor_list, name='profesor_list'),
    path('<int:pk>/', profesor_detail, name='profesor-detail'),   # Lista de estudiantes
    # Agrega otras rutas si es necesario
]
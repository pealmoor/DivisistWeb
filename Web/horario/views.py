# views.py en la app Horario
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Horario
from .serializers import HorarioSerializer
from django.shortcuts import render

class HorarioList(APIView):
    def get(self, request):
        # Obtener todos los horarios
        horarios = Horario.objects.all()
        serializer = HorarioSerializer(horarios, many=True)
        return Response(serializer.data)
class HorariosPorEstudiante(APIView):
    def get(self, request, estudiante_id):
        # Filtrar los horarios por el estudiante
        horarios = Horario.objects.filter(estudiante_id=estudiante_id)
        serializer = HorarioSerializer(horarios, many=True)
        return Response(serializer.data)

def horario_view(request):
    # Obtener todos los horarios de la base de datos (puedes agregar un filtro si es necesario)
    horarios = Horario.objects.all()  
    # Pasar los horarios al template
    return render(request, 'horario.html', {'horarios': horarios})

#



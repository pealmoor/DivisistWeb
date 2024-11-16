# serializers.py
from rest_framework import serializers
from .models import Horario

class HorarioSerializer(serializers.ModelSerializer):
    estudiante = serializers.StringRelatedField()  # Muestra el nombre completo del estudiante

    class Meta:
        model = Horario
        fields = ['estudiante', 'materia', 'salon', 'dia', 'hora_inicio', 'hora_fin']

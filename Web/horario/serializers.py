# horarios/serializers.py

from rest_framework import serializers
from .models import Horario, Nota


class HorarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Horario
        fields = ['id', 'materia', 'fecha', 'salon']

class NotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nota
        fields = ['id', 'nota']



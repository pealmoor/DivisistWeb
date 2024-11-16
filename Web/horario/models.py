# models.py en la app Horario
from django.db import models
from estudiante.models import Estudiante  # Asegúrate de importar el modelo Estudiante

class Horario(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE, null=True, blank=True)  # Relación con el modelo Estudiante
    materia = models.CharField(max_length=100)
    salon = models.CharField(max_length=50)
    dia = models.CharField(max_length=20, default='Monday')
    hora_inicio = models.TimeField(default='08:00:00')  # Ejemplo de valor predeterminado
    hora_fin = models.TimeField(default='10:00:00')

    def __str__(self):
        return f"{self.materia} - {self.dia} ({self.hora_inicio} - {self.hora_fin})"


    






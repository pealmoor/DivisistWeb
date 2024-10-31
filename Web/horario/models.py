from django.db import models

class Horario(models.Model):
    materia = models.CharField(max_length=100)
    fecha = models.DateTimeField()
    salon = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.materia} - {self.salon}'

class Nota(models.Model):
    horario = models.ForeignKey(Horario, on_delete=models.CASCADE, related_name='notas')
    nota = models.DecimalField(max_digits=5, decimal_places=2)
    
    def __str__(self):
        return f'Nota {self.nota} para {self.horario.materia}'
    






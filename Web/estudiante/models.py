# estudiante/models.py

from django.db import models

class Estudiante(models.Model):
    numeroidentificacion = models.CharField(max_length=20, unique=True)
    primerapellido = models.CharField(max_length=50)
    segundoapellido = models.CharField(max_length=50, blank=True, null=True)
    nombres = models.CharField(max_length=100)
    fechanacimiento = models.DateField()
    direccion = models.CharField(max_length=100)
    ciudadresidencia = models.CharField(max_length=50)
    telefono = models.CharField(blank=True, null=True)
    ciudadnacimiento = models.CharField(max_length=50)
    correoelectronico = models.EmailField(max_length=50,unique=True)
    carreraestudiando = models.CharField(max_length=100)
    nivelacademico = models.CharField(max_length=50)
  

    class Meta:
        db_table = 'estudiante'  

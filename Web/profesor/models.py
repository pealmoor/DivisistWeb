from django.db import models

# Create your models here.
class Profesor(models.Model):
    numeroidentificacion = models.CharField(max_length=20, unique=True)
    primerapellido = models.CharField(max_length=50)
    segundoapellido = models.CharField(max_length=50, blank=True, null=True)
    nombres = models.CharField(max_length=100)
    departamento= models.CharField(max_length=100)
    correoelectronico = models.EmailField(max_length=50,unique=True)

class Meta:
        db_table = 'profesor'   
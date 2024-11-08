from django.db import models


class Profesor(models.Model):
    numeroidentificacion = models.CharField(max_length=20, unique=True)
    primerapellido = models.CharField(max_length=50)
    segundoapellido = models.CharField(max_length=50, blank=True, null=True)
    nombres = models.CharField(max_length=100)
    departamento= models.CharField(max_length=100)
    correoelectronico = models.EmailField(max_length=50,unique=True)

class Meta:
        db_table = 'profesor'   

def __str__(self):
      
    return f"{self.nombres} {self.primerapellido} {self.segundoapellido or ''}".strip()
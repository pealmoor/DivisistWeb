# horarios/services.py

from .models import Estudiante
from .serializers import EstudianteSerializer
from rest_framework import status

def get_all_estudiantes():
    return Estudiante.objects.all()

def create_estudiante(data):
    serializer = EstudianteSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return serializer.data, status.HTTP_201_CREATED
    return serializer.errors, status.HTTP_400_BAD_REQUEST

def get_estudiante(pk):
    try:
        return Estudiante.objects.get(pk=pk)
    except Estudiante.DoesNotExist:
        return None

def update_estudiante(pk, data):
    estudiante = get_estudiante(pk)
    if estudiante:
        serializer = EstudianteSerializer(estudiante, data=data)
        if serializer.is_valid():
            serializer.save()
            return serializer.data, status.HTTP_200_OK
        return serializer.errors, status.HTTP_400_BAD_REQUEST
    return None, status.HTTP_404_NOT_FOUND

def delete_estudiante(pk):
    estudiante = get_estudiante(pk)
    if estudiante:
        estudiante.delete()
        return status.HTTP_204_NO_CONTENT
    return None, status.HTTP_404_NOT_FOUND

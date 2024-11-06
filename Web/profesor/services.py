from .models import Profesor
from .serializers import ProfesorSerializer
from rest_framework import status

def get_all_profesores():
    return Profesor.objects.all()

def create_profesor(data):
    serializer = ProfesorSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return serializer.data, status.HTTP_201_CREATED
    return serializer.errors, status.HTTP_400_BAD_REQUEST

def get_profesor(pk):
    try:
        return Profesor.objects.get(pk=pk)
    except Profesor.DoesNotExist:
        return None

def update_profesor(pk, data):
    profesor = get_profesor(pk)
    if profesor:
        serializer = ProfesorSerializer(profesor, data=data)
        if serializer.is_valid():
            serializer.save()
            return serializer.data, status.HTTP_200_OK
        return serializer.errors, status.HTTP_400_BAD_REQUEST
    return None, status.HTTP_404_NOT_FOUND

def delete_profesor(pk):
    profesor = get_profesor(pk)
    if profesor:
        profesor.delete()
        return status.HTTP_204_NO_CONTENT
    return None, status.HTTP_404_NOT_FOUND

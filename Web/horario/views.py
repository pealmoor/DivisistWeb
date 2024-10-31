# horarios/views.py

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Horario, Nota
from .serializers import HorarioSerializer, NotaSerializer

@api_view(['GET', 'POST'])
def horario_list(request):
    if request.method == 'GET':
        horarios = Horario.objects.all()
        serializer = HorarioSerializer(horarios, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = HorarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def horario_detail(request, pk):
    try:
        horario = Horario.objects.get(pk=pk)
    except Horario.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = HorarioSerializer(horario)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = HorarioSerializer(horario, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        horario.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def agregar_nota(request, pk):
    try:
        horario = Horario.objects.get(pk=pk)
    except Horario.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = NotaSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(horario=horario)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#



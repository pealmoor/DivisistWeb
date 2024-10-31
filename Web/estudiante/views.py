
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .services import (
    get_all_estudiantes,
    create_estudiante,
    get_estudiante,
    update_estudiante,
    delete_estudiante
)
from .serializers import EstudianteSerializer  # Asegúrate de importar también el serializador

@api_view(['GET', 'POST'])
def estudiante_list(request):
    if request.method == 'GET':
        estudiantes = get_all_estudiantes()
        serializer = EstudianteSerializer(estudiantes, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = request.data
        estudiante_data, status_code = create_estudiante(data)
        return Response(estudiante_data, status=status_code)

@api_view(['GET', 'PUT', 'DELETE'])
def estudiante_detail(request, pk):
    if request.method == 'GET':
        estudiante = get_estudiante(pk)
        if estudiante:
            serializer = EstudianteSerializer(estudiante)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)

    elif request.method == 'PUT':
        data = request.data
        updated_data, status_code = update_estudiante(pk, data)
        if updated_data:
            return Response(updated_data, status=status_code)
        return Response(status=status.HTTP_404_NOT_FOUND)

    elif request.method == 'DELETE':
        status_code = delete_estudiante(pk)
        if status_code == status.HTTP_204_NO_CONTENT:
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)

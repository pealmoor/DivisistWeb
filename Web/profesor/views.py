from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .services import (
    get_all_profesores,
    create_profesor,
    get_profesor,
    update_profesor,
    delete_profesor
)
from .serializers import ProfesorSerializer  

@api_view(['GET', 'POST'])
def profesor_list(request):
    if request.method == 'GET':
        profesores = get_all_profesores()
        serializer = ProfesorSerializer(profesores, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = request.data
        profesor_data, status_code = create_profesor(data)
        return Response(profesor_data, status=status_code)

@api_view(['GET', 'PUT', 'DELETE'])
def profesor_detail(request, pk):
    if request.method == 'GET':
        profesor = get_profesor(pk)
        if profesor:
            serializer = ProfesorSerializer(profesor)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)

    elif request.method == 'PUT':
        data = request.data
        updated_data, status_code = update_profesor(pk, data)
        if updated_data:
            return Response(updated_data, status=status_code)
        return Response(status=status.HTTP_404_NOT_FOUND)

    elif request.method == 'DELETE':
        status_code = delete_profesor(pk)
        if status_code == status.HTTP_204_NO_CONTENT:
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)
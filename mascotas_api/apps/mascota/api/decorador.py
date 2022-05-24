from rest_framework import status, permissions, authentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from mascotas_api.apps.mascota.api.serializers import MascotaSerializer, PersonaSerializer, VacunaSerializer

from mascotas_api.apps.mascota.models import Mascota
from rest_framework.response import Response
from django.http import Http404
from django.shortcuts import render, get_object_or_404


@api_view(['GET','POST'])
# @authentication_classes([authentication.SessionAuthentication])
# @permission_classes([permissions.IsAdminUser])
def lista_mascotas(request):

    '''
    ## LISTA DE MASCOTAS CON DECORADOR

    http://127.0.0.1:8000/api/decorador/mascotas/

    OK http POST http://127.0.0.1:8000/api/decorador/mascotas/ nombre="Loky" sexo="masculino" edad_aproximada="3" persona=1 raza=1 fecha_rescate="2022-07-11"
             
    Error serializer http POST http://127.0.0.1:8000/api/decorador/mascotas/ nombre="oso" sexo="masculino" edad_aproximada="3" persona=1 raza=1 fecha_rescate="2022-07-11"

    {

        "nombre": "Natsumi",
        "sexo": "Femenino",
        "edad": 1,
        "fecha_rescate": "2022-05-07",
        "persona": 1,
        "vacunas": [1]
    }
    '''
    if request.method == 'GET':
        mascotas = Mascota.objects.all()
        mascotas_json = MascotaSerializer(mascotas, many=True)
        return Response(mascotas_json.data)
    elif request.method == 'POST':
        mascotas_json = MascotaSerializer(data=request.data, partial=True)
        if mascotas_json.is_valid():
            mascotas_json.save()
            return Response(mascotas_json.data, status=status.HTTP_201_CREATED)
        return Response(mascotas_json.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
# @authentication_classes([authentication.SessionAuthentication])
# @permission_classes([permissions.IsAdminUser])
def detalle_mascota(request, pk):
    """

    ## DETALLE DE MASCOTA CON DECORADOR


    http http://127.0.0.1:8000/api/decorador/mascotas/4/

      
    OK http PUT http://127.0.0.1:8000/api/decorador/mascotas/4/ nombre="Loky" sexo="masculino" edad_aproximada="3" persona=1 raza=1 fecha_rescate="2022-07-11"

    ERROR enviando POST:  http POST http://127.0.0.1:8000/api/decorador/mascotas/4/ nombre="Loky" sexo="masculino" edad_aproximada="3" persona=1 raza=1 fecha_rescate="2022-07-11"


    {
        "id": 4,
        "nombre": "Natsumi 2",
        "sexo": "Femenino2",
        "edad_aproximada": 2,
        "fecha_rescate": "2022-05-07",
        "persona": 2,
        "vacuna": []
    }

    http DELETE http://127.0.0.1:8000/api/decorador/mascotas/17/
    """

    mascota = get_object_or_404(Mascota, pk=pk)


    if request.method == 'GET':
        serializer = MascotaSerializer(mascota)
        return Response(serializer.data)

    elif request.method == 'PUT' or request.method == 'PATCH':
        serializer = MascotaSerializer(mascota, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        mascota.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
# @authentication_classes([authentication.SessionAuthentication])
# @permission_classes([permissions.IsAdminUser])
def detalle_persona_mascota(request, pk):
    """
    ## DETALLE DE PERSONA CON DECORADOR
    http http://127.0.0.1:8000/api/decorador/mascotas/4/persona/

    """
    mascota = get_object_or_404(Mascota.objects.select_related('persona'), pk=pk)

    if request.method == 'GET':
        persona = mascota.persona
        if persona is not None:
            serializer = PersonaSerializer(persona)
            return Response(serializer.data)
        else:
            return Response({})
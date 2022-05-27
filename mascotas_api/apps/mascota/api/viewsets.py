# python packages

# django packages

# 3rd party packages

from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import action

# local packages

from mascotas_api.apps.mascota.api.serializers import MascotaSerializer, PersonaSerializer, VacunaSerializer

# Models

from mascotas_api.apps.mascota.models import Mascota, Vacuna
from mascotas_api.apps.adopcion.models import Persona


class MascotaViewSet(viewsets.ModelViewSet):
    """
    API endpoint que permite ver o editar mascotas (Viewsets)

    http://127.0.0.1:8000/api/viewsets/mascotas/

    OK http POST http://127.0.0.1:8000/api/viewsets/mascotas/ nombre="Loky" sexo="masculino" edad_aproximada="3" persona=1 raza=1 fecha_rescate="2022-07-11"
             
    Error serializer http POST http://127.0.0.1:8000/api/viewsets/mascotas/ nombre="oso" sexo="masculino" edad_aproximada="3" persona=1 raza=1 fecha_rescate="2022-07-11"

    {

        "nombre": "Natsumi",
        "sexo": "Femenino",
        "edad": 1,
        "fecha_rescate": "2022-05-07",
        "persona": 1,
        "vacunas": [1]
    }


    OK http PUT http://127.0.0.1:8000/api/viewsets/mascotas/4/ nombre="Loky" sexo="masculino" edad_aproximada="3" persona=1 raza=1 fecha_rescate="2022-07-11"

    ERROR enviando POST:  http POST http://127.0.0.1:8000/api/viewsets/mascotas/4/ nombre="Loky" sexo="masculino" edad_aproximada="3" persona=1 raza=1 fecha_rescate="2022-07-11"


    {
        "id": 4,
        "nombre": "Natsumi 2",
        "sexo": "Femenino2",
        "edad_aproximada": 2,
        "fecha_rescate": "2022-05-07",
        "persona": 2,
        "vacuna": []
    }

    http DELETE http://127.0.0.1:8000/api/viewsets/mascotas/17/


    http http://127.0.0.1:8000/api/genericview/mascotas/4/persona/

    """
    queryset = Mascota.objects.all()
    serializer_class = MascotaSerializer

    @action(
        detail=True,
        url_path='persona',
        url_name='persona')
    def persona(self, request, pk=None):
        serializer = PersonaSerializer(self.get_object().persona)
        return Response(serializer.data)

    @action(
        detail=True,
        url_path='vacuna',
        url_name='vacuna')
    def detail_vacuna(self, request, pk=None):
        serializer = VacunaSerializer(self.get_object().vacuna, many=True)
        return Response(serializer.data)




class PersonaViewSet(viewsets.ModelViewSet):
    """
    API endpoint que permite ver todas las personas (Viewsets)
    """
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer


class VacunaViewSet(viewsets.ModelViewSet):
    """
    API endpoint que permite ver todas las vacunas (Viewsets)
    """
    queryset = Vacuna.objects.all()
    serializer_class = VacunaSerializer


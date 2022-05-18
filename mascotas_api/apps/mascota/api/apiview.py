from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http import Http404
from rest_framework.views import APIView


from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated


from mascotas_api.apps.mascota.api.serializers import MascotaSerializer, PersonaSerializer
from mascotas_api.apps.mascota.models import Mascota
from mascotas_api.apps.adopcion.models import Persona

class MascotaListApiView(APIView):
    """
    Lista de todas las mascotas o crear una nueva mascota (APIView)
    """
    def get(self, request, format=None):
        '''
        http GET http://127.0.0.1:8000/api/apiview/mascotas/
        '''
        mascota = Mascota.objects.all()
        mascota_sr = MascotaSerializer(mascota, many=True)
        return Response(mascota_sr.data)

    def post(self, request, format=None):
        '''
        OK http POST http://127.0.0.1:8000/api/apiview/mascotas/ nombre="Loky" sexo="masculino" edad_aproximada="3" persona=1 raza=1 fecha_rescate="2022-07-11"
                 
        Error serializer http POST http://127.0.0.1:8000/api/apiview/mascotas/ nombre="oso" sexo="masculino" edad_aproximada="3" persona=1 raza=1 fecha_rescate="2022-07-11"

        {

            "nombre": "Natsumi",
            "sexo": "Femenino",
            "edad": 1,
            "fecha_rescate": "2022-05-07",
            "persona": 1,
            "vacunas": [1]
        }

        '''
        mascota_sr = MascotaSerializer(data=request.data)
        if mascota_sr.is_valid():
            mascota_sr.save()
            return Response(mascota_sr.data, status=status.HTTP_201_CREATED)
        return Response(mascota_sr.errors, status=status.HTTP_400_BAD_REQUEST)


class MascotaDetailApiView(APIView):
    """
    Obtener una mascota, actualizar o eliminar (APIView)
    """
    def get_object(self, pk):
        try:
            return Mascota.objects.get(pk=pk)
        except Mascota.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        """
        http http://127.0.0.1:8000/api/apiview/mascotas/4
        """
        mascota = self.get_object(pk)
        mascota_sr = MascotaSerializer(mascota)
        return Response(mascota_sr.data)

    def put(self, request, pk, format=None):
        """
        OK http PUT http://127.0.0.1:8000/api/apiview/mascotas/4 nombre="Loky" sexo="masculino" edad_aproximada="3" persona=1 raza=1 fecha_rescate="2022-07-11"
        ERROR enviando POST:  http POST http://127.0.0.1:8000/api/apiview/mascotas/4 nombre="Loky" sexo="masculino" edad_aproximada="3" persona=1 raza=1 fecha_rescate="2022-07-11"

        {
            "id": 4,
            "nombre": "Natsumi 2",
            "sexo": "Femenino2",
            "edad_aproximada": 2,
            "fecha_rescate": "2022-05-07",
            "persona": 2,
            "vacuna": []
        }
        """
        mascota = self.get_object(pk)
        mascota_sr = MascotaSerializer(mascota, data=request.data)
        if mascota_sr.is_valid():
            mascota_sr.save()
            return Response(mascota_sr.data)
        return Response(mascota_sr.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        """
        http DELETE http://127.0.0.1:8000/api/apiview/mascotas/5

        """
        mascota = self.get_object(pk)
        mascota.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class MascotaDetailPersonaApiView(APIView):
    """
    Obtener persona de la mascota (APIView)
    """
    def get_object(self, pk):
        try:
            return Persona.objects.filter(mascota=pk).first()
        except Persona.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        persona = self.get_object(pk=pk)
        persona_sr = PersonaSerializer(persona)
        return Response(persona_sr.data)
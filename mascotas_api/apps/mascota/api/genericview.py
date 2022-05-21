 

from mascotas_api.apps.mascota.api.serializers import MascotaSerializer, PersonaSerializer, VacunaSerializer
from mascotas_api.apps.mascota.models import Mascota, Vacuna
from mascotas_api.apps.adopcion.models import Persona


from rest_framework import mixins
from rest_framework import generics


class MascotaListGenericView(generics.ListCreateAPIView):
    """
    Lista de todas las mascotas o crear una nueva mascota (Generic ApiView)

    http://127.0.0.1:8000/api/genericview/mascotas/

    OK http POST http://127.0.0.1:8000/api/genericview/mascotas/ nombre="Loky" sexo="masculino" edad_aproximada="3" persona=1 raza=1 fecha_rescate="2022-07-11"
             
    Error serializer http POST http://127.0.0.1:8000/api/genericview/mascotas/ nombre="oso" sexo="masculino" edad_aproximada="3" persona=1 raza=1 fecha_rescate="2022-07-11"

    {

        "nombre": "Natsumi",
        "sexo": "Femenino",
        "edad": 1,
        "fecha_rescate": "2022-05-07",
        "persona": 1,
        "vacunas": [1]
    }

    """
    queryset = Mascota.objects.all()
    serializer_class = MascotaSerializer

    # def post(self, request, *args, **kwargs):
    #     print ("CREAMOS CON GENERICS")
    #     return self.create(request, *args, **kwargs)

class MascotaDetalleGenericView(generics.RetrieveUpdateDestroyAPIView):
    """
    Obtener una mascota, actualizar o eliminar (Generic ApiView)

    http http://127.0.0.1:8000/api/genericview/mascotas/4/

      
    OK http PUT http://127.0.0.1:8000/api/genericview/mascotas/4/ nombre="Loky" sexo="masculino" edad_aproximada="3" persona=1 raza=1 fecha_rescate="2022-07-11"

    ERROR enviando POST:  http POST http://127.0.0.1:8000/api/genericview/mascotas/4/ nombre="Loky" sexo="masculino" edad_aproximada="3" persona=1 raza=1 fecha_rescate="2022-07-11"


    {
        "id": 4,
        "nombre": "Natsumi 2",
        "sexo": "Femenino2",
        "edad_aproximada": 2,
        "fecha_rescate": "2022-05-07",
        "persona": 2,
        "vacuna": []
    }

    http DELETE http://127.0.0.1:8000/api/genericview/mascotas/17/

    """
    queryset = Mascota.objects.all()
    serializer_class = MascotaSerializer
 

    def put(self, request, *args, **kwargs):
        print ("ACTUALIZAMOS CON GENERICS")
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        print ("ELIMINAMOS CON GENERICS")
        return self.destroy(request, *args, **kwargs)

class MascotaDetallePersonaGenericView(generics.ListCreateAPIView):
    """
    Obtener persona de la mascota (Generic ApiView)
    http http://127.0.0.1:8000/api/genericview/mascotas/4/persona/
    
    """
    serializer_class = PersonaSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk', 0)
        queryset = Persona.objects.filter(mascota=pk)
        return queryset
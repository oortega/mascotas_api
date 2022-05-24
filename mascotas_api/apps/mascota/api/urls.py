 
from django.urls import path, include
from mascotas_api.apps.mascota.api.apiview import (MascotaListApiView,MascotaDetailApiView,
    MascotaDetailPersonaApiView)

from mascotas_api.apps.mascota.api.genericview import(MascotaListGenericView,MascotaDetalleGenericView,
    MascotaDetallePersonaGenericView)

from mascotas_api.apps.mascota.api.viewsets import (MascotaViewSet, PersonaViewSet, VacunaViewSet)

from mascotas_api.apps.mascota.api.decorador import(lista_mascotas,detalle_mascota, detalle_persona_mascota)
from rest_framework import routers
 
router = routers.DefaultRouter()
router.register(r'viewsets/mascotas', MascotaViewSet, basename="api-mascotas-viewsets")
urlpatterns = [
    # Decorador
    path('decorador/mascotas/', lista_mascotas, name="api-lista-mascotas-decorador"),
    path('decorador/mascotas/<int:pk>/', detalle_mascota, name="api-mascota-decorador"),
    path('decorador/mascotas/<int:pk>/persona/', detalle_persona_mascota, name="api-mascota-persona-decorador"),
    
    # APIView 
    path('apiview/mascotas/', MascotaListApiView.as_view(), name="api-lista-mascotas-apiview"),
    path('apiview/mascotas/<int:pk>/', MascotaDetailApiView.as_view(), name="api-mascota-apiview"),
    path('apiview/mascotas/<int:pk>/persona/', MascotaDetailPersonaApiView.as_view(), name="api-mascota-persona-apiview"),
   
    ## GenericView
    path('genericview/mascotas/', MascotaListGenericView.as_view(), name='api-lista-mascotas-genericview'),
    path('genericview/mascotas/<int:pk>/', MascotaDetalleGenericView.as_view(), name="api-mascota-genericview"),
    path('genericview/mascotas/<int:pk>/persona/', MascotaDetallePersonaGenericView.as_view(), name="api-mascota-persona-genericview"),

    ## ViewSets
    # path('', include(router.urls)),

    path('viewsets/mascotas/', MascotaViewSet.as_view({'get': 'list', 'post': 'create'}), name='api-lista-mascotas-viewsets'),
    path('viewsets/mascotas/<int:pk>/', MascotaViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='api-mascota-viewsets'),
    path('viewsets/mascotas/<int:pk>/persona/', MascotaViewSet.as_view({'get': 'persona'}), name='api-mascota-persona-viewsets'),

    # 
]

 

 

'''
listar en el menu - listo
endpoint de agregar-crud - listo
APIVIEW views agregar, listar, mascota, forms y templates - listo
Generic api y luego crud - listo
viewset api y luego crud - listo
decorador api y luego crud
ordenar dependencias segun el libro de twoscoops of django

'''
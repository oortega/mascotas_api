# from django.urls import path
from django.urls import path, include
from mascotas_api.apps.mascota.api.apiview import (MascotaListApiView,MascotaDetailApiView,
    MascotaDetailPersonaApiView)

from mascotas_api.apps.mascota.api.genericview import(MascotaListGenericView,MascotaDetalleGenericView,
    MascotaDetallePersonaGenericView)

from mascotas_api.apps.mascota.api.viewsets import (MascotaViewSet, PersonaViewSet, VacunaViewSet)

 

from rest_framework import routers

# from rest_framework.urlpatterns import format_suffix_patterns

# router = routers.DefaultRouter()
# router.register(r'v4/mascotas', MascotaViewSet, basename="api_mascotas_v4")
router = routers.DefaultRouter()
router.register(r'viewsets/mascotas', MascotaViewSet, basename="api-mascotas-viewsets")
urlpatterns = [
 
    
    ### APIView 
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

    # path('v2/mascotas/<int:pk>/', MascotaDetailAV.as_view()),
    # path('v2/mascotas/<int:pk>/persona/', MascotaDetailPersonaAV.as_view()),
    # path('v2/mascotas/<int:pk>/vacuna/', MascotaDetailVacunaAV.as_view()),
    # path('v2/personas/', PersonaListAV.as_view()),
    # path('v2/vacunas/', VacunaListAV.as_view()),
    # path('v3/mascotas/', MascotaListAVG.as_view(), name="api-v3-mascotas"),
    # path('v3/mascotas/<int:pk>/', MascotaDetailAVG.as_view()),
    # path('v3/mascotas/<int:pk>/persona/', MascotaDetailPersonaAVG.as_view()),
    # path('v3/mascotas/<int:pk>/vacuna/', MascotaDetailVacunaAVG.as_view()),
    # path('v3/personas/', PersonaListAVG.as_view()),
    # path('v3/vacunas/', VacunaListAVG.as_view()),
    # # path('v4/mascotas/<int:pk>/persona/', MascotaPersonaViewSet.as_view({'get': 'list'}), name="api-v4-mascotas"),
    # # path('v4/mascotas/<int:pk>/vacuna/', MascotaVacunaViewSet.as_view({'get': 'list'})),
    # path('v4/personas/', PersonaViewSet.as_view({'get': 'list'})),
    # path('v4/vacunas/', VacunaViewSet.as_view({'get': 'list'}))
    # path('', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

 

# urlpatterns = format_suffix_patterns(urlpatterns)

'''
listar en el menu - listo
endpoint de agregar-crud - listo
APIVIEW views agregar, listar, mascota, forms y templates - listo
Generic api y luego crud
viewset api y luego crud
decorador api y luego crud

'''
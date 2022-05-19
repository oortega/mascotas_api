# from django.urls import path
from django.urls import path, include
from mascotas_api.apps.mascota.api.apiview import (MascotaListApiView,MascotaDetailApiView,
    MascotaDetailPersonaApiView)

# from apps.mascota.api.view_apiviewd import (mascota_list_ad, mascota_detail_ad, mascota_detail_persona_ad,
#                                             mascota_detail_vacuna_ad, persona_list_ap, vacuna_list_ap)
# from apps.mascota.api.view_apiview import (MascotaListAV, MascotaDetailAV, MascotaDetailPersonaAV,
#                                            MascotaDetailVacunaAV, PersonaListAV, VacunaListAV)
# from apps.mascota.api.view_apiviewg import (MascotaListAVG, MascotaDetailAVG, MascotaDetailPersonaAVG,
#                                             MascotaDetailVacunaAVG, PersonaListAVG, VacunaListAVG)
# from apps.mascota.api.view_viewsets import (MascotaViewSet, PersonaViewSet, VacunaViewSet)

from rest_framework import routers

# from rest_framework.urlpatterns import format_suffix_patterns

# router = routers.DefaultRouter()
# router.register(r'v4/mascotas', MascotaViewSet, basename="api_mascotas_v4")

urlpatterns = [
    # path('v1/mascotas/', mascota_list_ad, name="api-v1-mascotas"),
    # path('v1/mascotas/<int:pk>/', mascota_detail_ad),
    # path('v1/mascotas/<int:pk>/persona/', mascota_detail_persona_ad),
    # path('v1/mascotas/<int:pk>/vacuna/', mascota_detail_vacuna_ad),
    # path('v1/personas/', persona_list_ap),
    # path('v1/vacunas/', vacuna_list_ap),
    
    ### APIView 
    path('apiview/mascotas/', MascotaListApiView.as_view(), name="apiview-lista-mascotas"),
    path('apiview/mascotas/<int:pk>/', MascotaDetailApiView.as_view(), name="apiview-mascota"),
    path('apiview/mascotas/<int:pk>/persona/', MascotaDetailPersonaApiView.as_view(), name="apiview-mascota-persona"),

    ### Termian APIView 

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

#urlpatterns += router.urls

# urlpatterns = format_suffix_patterns(urlpatterns)

'''
listar en el menu - listo
endpoint de agregar-crud - listo
views agregar, listar, mascota, forms y templates

'''
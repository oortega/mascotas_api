from django.urls import path, include
# from mascota.views import index, mascota_view, mascota_list, mascota_edit, mascota_delete, \
#     MascotaList, MascotaCreate, MascotaUpdate, MascotaDelete, VacunaList, VacunaCreate, VacunaUpdate, \
#     VacunaDelete, vacuna_view, vacuna_list, vacuna_edit, vacuna_delete, listado, listadousers
from mascotas_api.apps.mascota.views import (index_mascota,lista_mascotas_apiview, mascota_crear_apiview,
    mascota_editar_apiview,mascota_eliminar_apiview)


from mascotas_api.apps.mascota.views import (lista_mascotas_genericview,mascota_crear_genericview,
    mascota_editar_genericview,mascota_eliminar_genericview)
from mascotas_api.apps.mascota.views import(lista_mascotas_viewsets,mascota_crear_viewsets,
    mascota_editar_viewsets,mascota_eliminar_viewsets)

from mascotas_api.apps.mascota.views import(lista_mascotas_decorador, mascota_crear_decorador, 
    mascota_editar_decorador, mascota_eliminar_decorador)
app_name = 'mascotas'

urlpatterns = [
    path('', index_mascota, name="index"),
    # Decorador
    path('decorador/lista-mascotas/', lista_mascotas_decorador, name="lista_mascotas_decorador"),
    path('decorador/crear-mascotas/', mascota_crear_decorador, name="mascota_crear_decorador"),
    path('decorador/editar-mascotas/<int:id_mascota>/', mascota_editar_decorador, name="mascota_editar_decorador"),
    path('decorador/eliminar-mascotas/<int:id_mascota>/', mascota_eliminar_decorador, name="mascota_eliminar_decorador"),

    ## API VIEW
    path('apiview/lista-mascotas/', lista_mascotas_apiview, name="lista_mascotas_apiview"),
    path('apiview/crear-mascotas/', mascota_crear_apiview, name="mascota_crear_apiview"),
    path('apiview/editar-mascotas/<int:id_mascota>/', mascota_editar_apiview, name="mascota_editar_apiview"),
    path('apiview/eliminar-mascotas/<int:id_mascota>/', mascota_eliminar_apiview, name="mascota_eliminar_apiview"),

    # GenericView
    path('genericview/lista-mascotas/', lista_mascotas_genericview, name="lista_mascotas_genericview"),
    path('genericview/crear-mascotas/', mascota_crear_genericview, name="mascota_crear_genericview"),
    path('genericview/editar-mascotas/<int:id_mascota>/', mascota_editar_genericview, name="mascota_editar_genericview"),
    path('genericview/eliminar-mascotas/<int:id_mascota>/', mascota_eliminar_genericview, name="mascota_eliminar_genericview"),

    # ViewSets
    path('viewsets/lista-mascotas/', lista_mascotas_viewsets, name="lista_mascotas_viewsets"),
    path('viewsets/crear-mascotas/', mascota_crear_viewsets, name="mascota_crear_viewsets"),
    path('viewsets/editar-mascotas/<int:id_mascota>/', mascota_editar_viewsets, name="mascota_editar_viewsets"),
    path('viewsets/eliminar-mascotas/<int:id_mascota>/', mascota_eliminar_viewsets, name="mascota_eliminar_viewsets"),

 
]


 
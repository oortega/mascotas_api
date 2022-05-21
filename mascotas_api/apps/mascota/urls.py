from django.urls import path, include
# from mascota.views import index, mascota_view, mascota_list, mascota_edit, mascota_delete, \
#     MascotaList, MascotaCreate, MascotaUpdate, MascotaDelete, VacunaList, VacunaCreate, VacunaUpdate, \
#     VacunaDelete, vacuna_view, vacuna_list, vacuna_edit, vacuna_delete, listado, listadousers
from mascotas_api.apps.mascota.views import (index_mascota,lista_mascotas_apiview, mascota_crear_apiview,
    mascota_editar_apiview,mascota_eliminar_apiview)


from mascotas_api.apps.mascota.views import (lista_mascotas_genericview,mascota_crear_genericview,
    mascota_editar_genericview,mascota_eliminar_genericview)
app_name = 'mascotas'

urlpatterns = [
    path('', index_mascota, name="index"),
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
    # path('<str:api_v>/mascotas/crear/', mascota_create, name="mascota-create"),
    # path('<str:api_v>/mascotas/lista/', mascota_list, name="mascota-list"),
    # path('<str:api_v>/mascotas/elimina/<int:pk>/', mascota_delete, name="mascota-delete"),
    # path('<str:api_v>/mascotas/edita/<int:pk>/', mascota_edit, name="mascota-update"),
    # path('<str:api_v>/mascotas/<int:pk>/persona', mascota_persona, name="mascota-persona"),
    #url(r'', index, name="index"),
]


# path('<str:tipo_api>/lista-mascotas/', lista_mascotas_apiview, name="lista_mascotas_apiview"),
# path('<str:tipo_api>/crear-mascotas/', mascota_crear_apiview, name="mascota_crear_apiview"),
# path('<str:tipo_api>/editar-mascotas/<int:id_mascota>/apiview', mascota_editar_apiview, name="mascota_editar_apiview"),
# path('<str:tipo_api>/eliminar-mascotas/<int:id_mascota>/', mascota_eliminar_apiview, name="mascota_eliminar_apiview"),

# # GenericView
# path('<str:tipo_api>/lista-mascotas/', lista_mascotas_genericview, name="lista_mascotas_genericview"),
# path('<str:tipo_api>/crear-mascotas/', mascota_crear_genericview, name="mascota_crear_genericview"),
# path('<str:tipo_api>/editar-mascotas/<int:id_mascota>/', mascota_editar_genericview, name="mascota_editar_genericview"),
# path('<str:tipo_api>/eliminar-mascotas/<int:id_mascota>/', mascota_eliminar_genericview, name="mascota_eliminar_genericview"),
# # path('<
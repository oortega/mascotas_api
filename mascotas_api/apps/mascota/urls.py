from django.urls import path, include
# from mascota.views import index, mascota_view, mascota_list, mascota_edit, mascota_delete, \
#     MascotaList, MascotaCreate, MascotaUpdate, MascotaDelete, VacunaList, VacunaCreate, VacunaUpdate, \
#     VacunaDelete, vacuna_view, vacuna_list, vacuna_edit, vacuna_delete, listado, listadousers
from mascotas_api.apps.mascota.views import index_mascota

app_name = 'mascotas'

urlpatterns = [
    path('', index_mascota, name="index"),
    # path('<str:api_v>/mascotas/crear/', mascota_create, name="mascota-create"),
    # path('<str:api_v>/mascotas/lista/', mascota_list, name="mascota-list"),
    # path('<str:api_v>/mascotas/elimina/<int:pk>/', mascota_delete, name="mascota-delete"),
    # path('<str:api_v>/mascotas/edita/<int:pk>/', mascota_edit, name="mascota-update"),
    # path('<str:api_v>/mascotas/<int:pk>/persona', mascota_persona, name="mascota-persona"),
    #url(r'', index, name="index"),
]

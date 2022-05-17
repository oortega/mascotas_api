from django.contrib import admin
from mascotas_api.apps.mascota.models import Vacuna, Mascota, Raza#, Persona
     
# Register your models here.

admin.site.register(Vacuna)
admin.site.register(Mascota)
admin.site.register(Raza)
#admin.site.register(Persona)
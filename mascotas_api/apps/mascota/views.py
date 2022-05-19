import json

from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
# from rest_framework.parsers import JSONParser
# from rest_framework.request import Request

# from app.API.view.view_apiview import ListMascotas, DetalleMascota, MascotaPersonaList
# from app.API.view.view_decorador import list_mascotas, detail_mascota, mascota_persona_list
# from app.API.view.view_generic import MascotaListGeneric, MascotaDetailsGeneric, MascotaPersonaListGeneric
# from app.API.view.view_set import MascotaViewset

from mascotas_api.apps.mascota.forms import MascotaForm
from mascotas_api.apps.mascota.api.apiview import (MascotaListApiView,MascotaDetailApiView,
    MascotaDetailPersonaApiView)

# from app.mascota.models import Mascota
# from django.views.generic import ListView, CreateView, UpdateView, DeleteView
# from django.core.urlresolvers import reverse_lazy

# Rest Framework
from rest_framework import status


# -----------funciones-------------------
def index_mascota(request):
    return render(request, 'mascota_home.html')

# APIView 
def lista_mascotas_apiview(request):
    data = MascotaListApiView.as_view()(request).data
    return render(request, 'lista_mascotas.html',{'lista_mascotas': data})

def mascota_crear_apiview(request):
    
    form = MascotaForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            mascota_instance = MascotaListApiView.as_view()(request)

            if mascota_instance.status_code == status.HTTP_201_CREATED:
                messages.success(request, "Se agrego correctamente la mascota")
                return HttpResponseRedirect((reverse('mascotas:lista_mascotas_apiview', )))

            else:
                serializers_errors = mascota_instance.data.serializer.errors
                for error in serializers_errors:
                    if error == 'non_field_errors':
                        form.add_error('__all__', serializers_errors.get(error)[0])
                    else:
                        form.add_error(error, serializers_errors.get(error)[0])
     
    return render(request, 'mascota_form.html', {'form': form, "tipo": "ApiView"})

# Termina APIView
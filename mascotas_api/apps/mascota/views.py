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

def mascota_editar_apiview(request, id_mascota):
    if request.method == "POST":
        form = MascotaForm(request.POST)
     

        if form.is_valid():
            """
            Hay que espeficarle el resquest.method ya que la API tiene varios protocolos HTTP y no acepta el POST para
            realizar esta peticion
            """
            request.method = "PUT"

            mascota_instance = MascotaDetailApiView().as_view()(request, id_mascota)
            

            if mascota_instance.status_code == status.HTTP_200_OK:
                messages.success(request, "Se actualizo correctamente la mascota {0}".format(id_mascota))
                return HttpResponseRedirect((reverse('mascotas:lista_mascotas_apiview', )))

            else:
                serializers_errors = mascota_instance.data.serializer.errors
                for error in serializers_errors:
                    if error == 'non_field_errors':
                        form.add_error('__all__', serializers_errors.get(error)[0])
                    else:
                        form.add_error(error, serializers_errors.get(error)[0])
    else:
        mascota_instance = MascotaDetailApiView()
        mascota_instance = mascota_instance.get(request, pk=id_mascota) # aqui como seria MacotaDetailApiView.as_view()(request, id_mascota).data ?
        persona = ""
        if mascota_instance.data.get('persona', {}):
            persona = mascota_instance.data.get('persona', {}).get('id')
        initial = {
            **mascota_instance.data,
            'persona': persona, #mascota_instance.data.get('persona', {}).get('id'),
            'vacunas': map(lambda vacuna: vacuna.get('id'),
                           mascota_instance.data.get('vacunas', list())),
        }
        form = MascotaForm(initial=initial)

    return render(request, 'mascota_form.html', {'form': form, "tipo": "ApiView"})

def mascota_eliminar_apiview(request, id_mascota):
    if request.method == "POST":

        request.method = 'DELETE'

        mascota_instance = MascotaDetailApiView.as_view()(request, id_mascota)
        if mascota_instance.status_code == status.HTTP_204_NO_CONTENT:
            messages.success(request, "Se elimino correctamente la mascota {0} - {1}".format(str(mascota_instance), mascota_instance.status_code))
        else:
            messages.error(request, "No se puedo  elimino correctamente la mascota {0} por favor intenta mas tarde. {1}".format(str(mascota_instance), mascota_instance.status_code))

            
        return HttpResponseRedirect((reverse('mascotas:lista_mascotas_apiview', )))


    else:
        mascota_instance = MascotaDetailApiView.as_view()(request, id_mascota).data  
    return render(request, 'mascota_eliminar.html',{ 'mascota': mascota_instance, "tipo": "APIView"})

# Termina APIView
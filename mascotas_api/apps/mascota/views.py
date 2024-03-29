# python packages

import json

# django packages

from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages




# 3rd party packages

from rest_framework import status
 
# local packages

from mascotas_api.apps.mascota.forms import MascotaForm
from mascotas_api.apps.mascota.api.apiview import (MascotaListApiView,MascotaDetailApiView,
    MascotaDetailPersonaApiView)
from mascotas_api.apps.mascota.api.genericview import(MascotaListGenericView,MascotaDetalleGenericView,
    MascotaDetallePersonaGenericView)
from mascotas_api.apps.mascota.api.viewsets import MascotaViewSet
from mascotas_api.apps.mascota.api.decorador import (lista_mascotas, detalle_mascota, detalle_persona_mascota)

# Models
 

# -----------funciones-------------------
def index_mascota(request):
    return render(request, 'mascota_home.html')
 
# Decorador
def lista_mascotas_decorador(request ):
    data = lista_mascotas(request).data
    return render(request, 'lista_mascotas.html',{'lista_mascotas': data, 'tipo': 'decorador'})

def mascota_crear_decorador(request):
    form = MascotaForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            mascota_instance = lista_mascotas(request)

            if mascota_instance.status_code == status.HTTP_201_CREATED:
                messages.success(request, "Se agrego correctamente la mascota usando decorador")
                return HttpResponseRedirect((reverse('mascotas:lista_mascotas_decorador', )))

            else:
                serializers_errors = mascota_instance.data.serializer.errors
                for error in serializers_errors:
                    if error == 'non_field_errors':
                        form.add_error('__all__', serializers_errors.get(error)[0])
                    else:
                        form.add_error(error, serializers_errors.get(error)[0])
     
    return render(request, 'mascota_form.html', {'form': form, 'tipo': 'decorador'})

def mascota_editar_decorador(request, id_mascota):
    if request.method == "POST":
        form = MascotaForm(request.POST)
     

        if form.is_valid():
            """
            Hay que espeficarle el resquest.method ya que la API tiene varios protocolos HTTP y no acepta el POST para
            realizar esta peticion
            """
            request.method = "PUT"

            mascota_instance = detalle_mascota(request, id_mascota)
            

            if mascota_instance.status_code == status.HTTP_200_OK:
                messages.success(request, "Se actualizo correctamente la mascota {0} usando decorador".format(id_mascota))
                return HttpResponseRedirect((reverse('mascotas:lista_mascotas_decorador', )))

            else:
                serializers_errors = mascota_instance.data.serializer.errors
                for error in serializers_errors:
                    if error == 'non_field_errors':
                        form.add_error('__all__', serializers_errors.get(error)[0])
                    else:
                        form.add_error(error, serializers_errors.get(error)[0])
    else:
        
        mascota_instance = detalle_mascota(request, pk=id_mascota) # aqui como seria MacotaDetailApiView.as_view()(request, id_mascota).data ?
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

    return render(request, 'mascota_form.html', {'form': form, 'tipo': 'decorador'})

def mascota_eliminar_decorador(request, id_mascota):
    if request.method == "POST":

        request.method = 'DELETE'

        mascota_instance = detalle_mascota(request, id_mascota)
        if mascota_instance.status_code == status.HTTP_204_NO_CONTENT:
            messages.success(request, "Se elimino correctamente la mascota {0} - {1} usando decorador".format(str(mascota_instance), mascota_instance.status_code))
        else:
            messages.error(request, "No se puedo  elimino correctamente la mascota {0} por favor intenta mas tarde. {1}".format(str(mascota_instance), mascota_instance.status_code))

            
        return HttpResponseRedirect((reverse('mascotas:lista_mascotas_decorador', )))


    else:
        mascota_instance = detalle_mascota(request, id_mascota).data  
    return render(request, 'mascota_eliminar.html',{ 'mascota': mascota_instance, 'tipo': 'decorador'})

# APIView 
def lista_mascotas_apiview(request ):
    data = MascotaListApiView.as_view()(request).data
    return render(request, 'lista_mascotas.html',{'lista_mascotas': data, 'tipo': 'apiview'})

def mascota_crear_apiview(request ):
    
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
     
    return render(request, 'mascota_form.html', {'form': form, 'tipo': 'apiview'})

def mascota_editar_apiview(request,  id_mascota):
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

    return render(request, 'mascota_form.html', {'form': form, 'tipo': 'apiview'})

def mascota_eliminar_apiview(request,  id_mascota):
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
    return render(request, 'mascota_eliminar.html',{ 'mascota': mascota_instance, 'tipo': 'apiview'})

# Termina APIView


# GenericView

def lista_mascotas_genericview(request ):
    data = MascotaListGenericView.as_view()(request).data
    return render(request, 'lista_mascotas.html',{'lista_mascotas': data, 'tipo': 'genericview' })

def mascota_crear_genericview(request ):
    
    form = MascotaForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            mascota_instance = MascotaListGenericView.as_view()(request)

            if mascota_instance.status_code == status.HTTP_201_CREATED:
                messages.success(request, "Se agrego correctamente la mascota")
                return HttpResponseRedirect((reverse('mascotas:lista_mascotas_genericview', )))

            else:
                serializers_errors = mascota_instance.data.serializer.errors
                for error in serializers_errors:
                    if error == 'non_field_errors':
                        form.add_error('__all__', serializers_errors.get(error)[0])
                    else:
                        form.add_error(error, serializers_errors.get(error)[0])
     
    return render(request, 'mascota_form.html', {'form': form, 'tipo': 'genericview'})
    #return render(request, 'lista_mascotas.html',{'lista_mascotas': data, 'tipo': 'genericview' })

def mascota_editar_genericview(request,  id_mascota): 
    
    if request.method == "POST":
        form = MascotaForm(request.POST)
     

        if form.is_valid():
            """
            Hay que espeficarle el resquest.method ya que la API tiene varios protocolos HTTP y no acepta el POST para
            realizar esta peticion
            """
            request.method = "PUT"

            mascota_instance = MascotaDetalleGenericView.as_view()(request=request, pk=id_mascota)
            

            if mascota_instance.status_code == status.HTTP_200_OK:
                messages.success(request, "Se actualizo correctamente la mascota {0}".format(id_mascota))
                return HttpResponseRedirect((reverse('mascotas:lista_mascotas_genericview', )))

            else:
                serializers_errors = mascota_instance.data.serializer.errors
                for error in serializers_errors:
                    if error == 'non_field_errors':
                        form.add_error('__all__', serializers_errors.get(error)[0])
                    else:
                        form.add_error(error, serializers_errors.get(error)[0])
    else:
        mascota_instance = MascotaDetalleGenericView.as_view()(request=request, pk=id_mascota)
        #mascota_instance = mascota_instance.get(request, pk=id_mascota) # aqui como seria MacotaDetailApiView.as_view()(request, id_mascota).data ?
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

    return render(request, 'mascota_form.html', {'form': form, 'tipo': 'genericview'})

    

def mascota_eliminar_genericview(request,  id_mascota):
    
    if request.method == "POST":

        request.method = 'DELETE'

        mascota_instance = MascotaDetalleGenericView.as_view()(request=request, pk=id_mascota)
        if mascota_instance.status_code == status.HTTP_204_NO_CONTENT:
            messages.success(request, "Se elimino correctamente la mascota {0} - {1}".format(str(mascota_instance), mascota_instance.status_code))
        else:
            messages.error(request, "No se puedo  elimino correctamente la mascota {0} por favor intenta mas tarde. {1}".format(str(mascota_instance), mascota_instance.status_code))

            
        return HttpResponseRedirect((reverse('mascotas:lista_mascotas_genericview', )))


    else:
        mascota_instance = MascotaDetalleGenericView.as_view()(request=request, pk=id_mascota).data  
    return render(request, 'mascota_eliminar.html',{ 'mascota': mascota_instance, 'tipo': 'genericview'})

## ViewSets

def lista_mascotas_viewsets(request ):
    data = MascotaViewSet.as_view({'get': 'list'})(request).data
    return render(request, 'lista_mascotas.html',{'lista_mascotas': data, 'tipo': 'viewsets' })

def mascota_crear_viewsets(request ):
    
    form = MascotaForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            mascota_instance = MascotaViewSet.as_view({'post': 'create'})(request)

            if mascota_instance.status_code == status.HTTP_201_CREATED:
                messages.success(request, "Se agrego correctamente la mascota")
                return HttpResponseRedirect((reverse('mascotas:lista_mascotas_viewsets', )))

            else:
                serializers_errors = mascota_instance.data.serializer.errors
                for error in serializers_errors:
                    if error == 'non_field_errors':
                        form.add_error('__all__', serializers_errors.get(error)[0])
                    else:
                        form.add_error(error, serializers_errors.get(error)[0])
     
    return render(request, 'mascota_form.html', {'form': form, 'tipo': 'viewsets'})

def mascota_editar_viewsets(request,  id_mascota): 
    
    if request.method == "POST":
        form = MascotaForm(request.POST)
     

        if form.is_valid():
            """
            Hay que espeficarle el resquest.method ya que la API tiene varios protocolos HTTP y no acepta el POST para
            realizar esta peticion
            """
            request.method = "PUT"

            mascota_instance = MascotaViewSet.as_view({'put': 'update'})(request=request, pk=id_mascota)
            

            if mascota_instance.status_code == status.HTTP_200_OK:
                messages.success(request, "Se actualizo correctamente la mascota {0}".format(id_mascota))
                return HttpResponseRedirect((reverse('mascotas:lista_mascotas_viewsets', )))

            else:
                serializers_errors = mascota_instance.data.serializer.errors
                for error in serializers_errors:
                    if error == 'non_field_errors':
                        form.add_error('__all__', serializers_errors.get(error)[0])
                    else:
                        form.add_error(error, serializers_errors.get(error)[0])
    else:
        mascota_instance = MascotaViewSet.as_view({'get': 'retrieve'})(request=request, pk=id_mascota)
        #mascota_instance = mascota_instance.get(request, pk=id_mascota) # aqui como seria MacotaDetailApiView.as_view()(request, id_mascota).data ?
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

    return render(request, 'mascota_form.html', {'form': form, 'tipo': 'viewsets'})

    

def mascota_eliminar_viewsets(request,  id_mascota):
    
    if request.method == "POST":

        request.method = 'DELETE'

        mascota_instance = MascotaViewSet.as_view({'delete': 'destroy'})(request=request, pk=id_mascota)
        if mascota_instance.status_code == status.HTTP_204_NO_CONTENT:
            messages.success(request, "Se elimino correctamente la mascota {0} - {1} con viewsets".format(str(mascota_instance), mascota_instance.status_code))
        else:
            messages.error(request, "No se puedo  elimino correctamente la mascota {0} por favor intenta mas tarde. {1}".format(str(mascota_instance), mascota_instance.status_code))

            
        return HttpResponseRedirect((reverse('mascotas:lista_mascotas_viewsets', )))


    else:
        mascota_instance = MascotaViewSet.as_view({'get': 'retrieve'})(request=request, pk=id_mascota).data  
    return render(request, 'mascota_eliminar.html',{ 'mascota': mascota_instance, 'tipo': 'viewsets'})    
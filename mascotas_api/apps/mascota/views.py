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
# from app.mascota.forms import MascotaForm, MascotaApiForm
# from app.mascota.models import Mascota
# from django.views.generic import ListView, CreateView, UpdateView, DeleteView
# from django.core.urlresolvers import reverse_lazy

# # Rest Framework
# from rest_framework import status


# -----------funciones-------------------
def index_mascota(request):
    return render(request, 'mascota_home.html')
# python packages

from __future__ import unicode_literals

# django packages

from django.db import models

# 3rd party packages

# local packages

# Models

# Create your models here.


class Persona(models.Model):
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=70)
    edad = models.IntegerField()
    telefono = models.CharField(max_length=12)
    email = models.EmailField()
    domicilio = models.TextField()

    def __str__(self):
        return '{} {}'.format(self.nombre,self.apellidos)

class Solicitud(models.Model):
    persona = models.ForeignKey(Persona, null=True, blank=True, on_delete=models.CASCADE)
    numero_mascotas = models.IntegerField()
    razones = models.TextField()

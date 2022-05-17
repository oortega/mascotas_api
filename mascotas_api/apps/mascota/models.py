from __future__ import unicode_literals

from django.db import models
from mascotas_api.apps.adopcion.models import Persona


# Create your models here.
class Vacuna(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return '{}'.format(self.nombre)


def upload_location(instance, filename):
    filebase, extension = filename.split('.')
    return '%s-%s-%s.%s' %(instance.persona, instance.nombre, instance.fecha_rescate, extension)


class Raza(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return '{}'.format(self.nombre)


class Mascota(models.Model):
    # folio = models.CharField(max_length=10,primary_key=True)
    nombre = models.CharField(max_length=50, null=True, blank=True)
    sexo = models.CharField(max_length=10, null=True, blank=True)
    edad_aproximada = models.IntegerField(null=True, blank=True)
    fecha_rescate = models.DateField(null=True, blank=True)
    persona = models.ForeignKey(Persona, null=True, blank=True, on_delete=models.CASCADE)
    vacuna = models.ManyToManyField(Vacuna, null=True, blank=True)
    # raza = models.ForeignKey(Raza, null=True, blank=True, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to=upload_location, null=True, blank=True)

    class Meta:
        ordering = ('-id',)

    def __str__(self):
        return '{}'.format(self.nombre)
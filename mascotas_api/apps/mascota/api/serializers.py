# python packages

# django packages

from django.contrib.auth.models import User, Group

# 3rd party packages

from rest_framework import serializers

# local packages

# Models

from mascotas_api.apps.mascota.models import Mascota, Vacuna
from mascotas_api.apps.adopcion.models import Persona




class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = "__all__"

class VacunaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacuna
        fields = "__all__"

class MascotaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Mascota
        fields = ('id', 'nombre', 'sexo', 'edad_aproximada', 'fecha_rescate', 'persona', 'vacuna')

    def validate(self, data):
        """
        validacion de general de prueba
        """
        if data["nombre"] == "oso":
            raise serializers.ValidationError("Oso es una palabra reservada, por favor introduce otro valor.")

        return data

    def to_representation(self, instance):
        self.fields['persona'] = PersonaSerializer(read_only=True, required=False)
        self.fields['vacuna'] = VacunaSerializer(read_only=True, many=True)
        # self.fields['raza'] = RazaSerializer(read_only=True, required=False)
        return super(MascotaSerializer, self).to_representation(instance)

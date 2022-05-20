from django import forms
from django.forms.fields import ChoiceField, MultipleChoiceField

from mascotas_api.apps.mascota.models import Mascota, Vacuna
from mascotas_api.apps.adopcion.models import Persona



class ChoiceFieldNoValidation(ChoiceField):
    def validate(self, value):
        pass


class MascotaForm(forms.Form):
    TIPO_SEXO = (
        ('Macho', 'Macho'),
        ('Hembra', 'Hembra'),
    )
    error_css_class = "error"
    nombre = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    
    sexo = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}), required=False, choices=TIPO_SEXO)
    edad_aproximada = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    fecha_rescate = forms.DateField(widget=forms.TextInput(attrs={'class': 'form-control', 'type':'date'}), required=False)
 
    persona = forms.ModelChoiceField(widget=forms.Select(attrs={'class': 'form-control'}), queryset=Persona.objects.all(), required=False)
    vacuna = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple(), required=False, queryset=Vacuna.objects.all())
# institucion/app_institucion/forms.py
from django import forms
from .models import Institucion, Servicio, Curso

class InstitucionForm(forms.ModelForm):
    class Meta:
        model = Institucion
        fields = ['nombre', 'direccion', 'telefono', 'email', 'descripcion']

class ServicioForm(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = ['institucion', 'nombre', 'descripcion']

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['institucion', 'nombre', 'descripcion', 'duracion']
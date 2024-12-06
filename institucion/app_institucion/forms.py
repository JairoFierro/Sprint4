# institucion/app_institucion/forms.py
from django import forms
from .models import Estudiante, Institucion, Servicio, Curso

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
        # institucion/app_institucion/forms.py

class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = ['nombre', 'email', 'telefono']  # Campos que deseas incluir en el formulario
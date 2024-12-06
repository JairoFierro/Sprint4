# institucion/app_institucion/urls.py
from django.urls import path
from .views import crear_institucion, listar_instituciones, actualizar_institucion,crear_estudiante, bienvenida, institucion
urlpatterns = [
    #path('', listar_instituciones, name='listar_instituciones'),  # Ruta para listar instituciones
    path('', bienvenida, name='bienvenida'),
    path('instituciones/', institucion, name='institucion'),
    path('crear/', crear_institucion, name='crear_institucion'),  # Ruta para crear institución
    #path('actualizar/<int:institucion_id>/', actualizar_institucion, name='actualizar_institucion'),  # Ruta para actualizar
    path('crear-estudiante/', crear_estudiante, name='crear_estudiante'),  # Nueva ruta para crear estudiante
    path('listar-instituciones/', listar_instituciones, name='listar_instituciones'),  # Add this line

]
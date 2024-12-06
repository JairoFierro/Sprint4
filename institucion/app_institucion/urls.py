# institucion/app_institucion/urls.py
from django.urls import path
from .views import crear_institucion, listar_instituciones, actualizar_institucion

urlpatterns = [
    path('crear-institucion/', crear_institucion, name='crear_institucion'),
    path('listar-instituciones/', listar_instituciones, name='listar_instituciones'),
    path('actualizar-institucion/<int:institucion_id>/', actualizar_institucion, name='actualizar_institucion'),
]
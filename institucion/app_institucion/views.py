from django.shortcuts import render, redirect, get_object_or_404
from .models import Institucion, Servicio, Curso
from .forms import InstitucionForm, ServicioForm, CursoForm

def crear_institucion(request):
    if request.method == 'POST':
        form = InstitucionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_instituciones')
    else:
        form = InstitucionForm()
    return render(request, 'institucion/crear_institucion.html', {'form': form})

def listar_instituciones(request):
    instituciones = Institucion.objects.all()
    return render(request, 'institucion/listar_instituciones.html', {'instituciones': instituciones})

def actualizar_institucion(request, institucion_id):
    institucion = get_object_or_404(Institucion, id=institucion_id)
    if request.method == 'POST':
        form = InstitucionForm(request.POST, instance=institucion)
        if form.is_valid():
            form.save()
            return redirect('listar_instituciones')
    else:
        form = InstitucionForm(instance=institucion)
    return render(request, 'institucion/crear_institucion.html', {'form': form})

# Similarmente, puedes crear vistas para Servicios y Cursos
from django.shortcuts import render, redirect, get_object_or_404
from .models import Estudiante, Institucion, Servicio, Curso
from .forms import EstudianteForm, InstitucionForm, ServicioForm, CursoForm


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



def crear_estudiante(request):
    if request.method == 'POST':
        form = EstudianteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_estudiantes')  
    else:
        form = EstudianteForm()
    
    return render(request, 'institucion/crear_estudiante.html', {'form': form})
# institucion/app_institucion/views.py
def listar_estudiantes(request):
    estudiantes = Estudiante.objects.all()
    return render(request, 'institucion/listar_estudiantes.html', {'estudiantes': estudiantes})

def bienvenida(request):
    return render(request, 'institucion/bienvenido.html')

def institucion(request):
    return render(request, 'institucion/institucion.html')
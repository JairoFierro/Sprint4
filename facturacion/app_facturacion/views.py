from django.shortcuts import render, redirect
from .models import Estudiante, Factura, Recibo
from .forms import EstudianteForm, FacturaForm, ReciboForm

def crear_factura(request):
    if request.method == 'POST':
        form = FacturaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_facturas')
    else:
        form = FacturaForm()
    
    estudiantes = Estudiante.objects.all()  # Obtiene todos los estudiantes
    return render(request, 'facturacion/crear_factura.html', {'form': form, 'estudiantes': estudiantes})

def listar_facturas(request):
    facturas = Factura.objects.all()
    return render(request, 'facturacion/listar_facturas.html', {'facturas': facturas})

def crear_recibo(request, factura_id):
    factura = Factura.objects.get(id=factura_id)
    if request.method == 'POST':
        form = ReciboForm(request.POST)
        if form.is_valid():
            recibo = form.save(commit=False)
            recibo.factura = factura
            recibo.save()
            return redirect('listar_facturas')
    else:
        form = ReciboForm()
    return render(request, 'facturacion/crear_recibo.html', {'form': form, 'factura': factura})

def vista_principal(request):
    return render(request, 'facturacion/vista_principal.html')  

def crear_estudiante(request):
    if request.method == 'POST':
        form = EstudianteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_estudiantes')  # Redirige a una vista que liste estudiantes
    else:
        form = EstudianteForm()
    
    return render(request, 'facturacion/crear_estudiante.html', {'form': form})
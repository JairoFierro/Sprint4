from django.shortcuts import render, redirect
from .models import Factura, Recibo
from .forms import FacturaForm, ReciboForm
# app_facturacion/views.py

def crear_factura(request):
    if request.method == 'POST':
        form = FacturaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_facturas')
    else:
        form = FacturaForm()
    return render(request, 'facturacion/crear_factura.html', {'form': form})

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
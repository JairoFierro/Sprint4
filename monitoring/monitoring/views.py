from django.shortcuts import render, redirect, get_object_or_404


def redirect_to_instituciones(request):
    # Redirigir al servicio de instituciones
    return redirect('http://34.136.35.99:8000/instituciones')


def redirect_to_facturacion(request):
    # Redirigir al servicio de facturación
    return redirect('http://34.136.35.99:8000/facturacion')
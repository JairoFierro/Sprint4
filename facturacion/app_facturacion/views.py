from django.shortcuts import render, redirect
from .models import Factura, Recibo
from .forms import FacturaForm, ReciboForm
import pika
import json
from django.conf import settings

# app_facturacion/views.py

def crear_factura(request):
    if request.method == 'POST':
        form = FacturaForm(request.POST)
        if form.is_valid():
            factura = form.save()
            enviar_notificacion(factura)
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

def enviar_notificacion(factura):
    try:
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(
                host=settings.RABBITMQ['HOST'],
                port=settings.RABBITMQ['PORT'],
                credentials=pika.PlainCredentials(settings.RABBITMQ['USER'], settings.RABBITMQ['PASSWORD'])
            )
        )
        channel = connection.channel()

        channel.queue_declare(queue=settings.RABBITMQ['QUEUE'])

        mensaje = {
            'email': 'istorkyt@gmail.com',  # Correo estático como se solicitó
            'tipo': 'factura_pendiente',
            'contenido': f'La factura {factura.id} está pendiente de pago.'
        }

        channel.basic_publish(
            exchange='',
            routing_key=settings.RABBITMQ['QUEUE'],
            body=json.dumps(mensaje)
        )

        connection.close()

    except Exception as e:
        print(f"Error al enviar notificación: {e}")
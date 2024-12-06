from django.db import models
from datetime import datetime

class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.nombre

class Notificacion(models.Model):
    NOTIFICACION_TIPOS = [
        ('recordatorio', 'Recordatorio de Pago'),
        ('confirmacion_pago', 'Confirmación de Pago'),
        ('retraso_pago', 'Retraso en Pago'),
        ('factura_generada', 'Factura Generada'),
    ]
    
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=20, choices=NOTIFICACION_TIPOS)
    mensaje = models.TextField()
    fecha_envio = models.DateTimeField(default=datetime.now)
    estado = models.CharField(max_length=20, choices=[
        ('enviado', 'Enviado'),
        ('pendiente', 'Pendiente'),
        ('fallido', 'Fallido'),
    ], default='pendiente')

    def __str__(self):
        return f'Notificación a {self.estudiante.nombre} - {self.get_tipo_display()}'

    def enviar(self):
        try:
            print(f"Enviando notificación a {self.estudiante.email}: {self.mensaje}")
            self.estado = 'enviado'
            self.save()
        except Exception as e:
            self.estado = 'fallido'
            self.save()
            print(f"Error al enviar notificación: {e}")

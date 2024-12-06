from django import forms
from .models import Factura, Recibo,Estudiante

class FacturaForm(forms.ModelForm):
    class Meta:
        model = Factura
        fields = ['estudiante', 'monto_total', 'fecha_vencimiento', 'estado']  
class ReciboForm(forms.ModelForm):
    class Meta:
        model = Recibo
        fields = ['fecha_pago', 'monto_pagado']

class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = ['nombre', 'email']  # Campos que deseas incluir en el formulario
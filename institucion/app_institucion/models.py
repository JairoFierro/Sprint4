# institucion/app_institucion/models.py
from django.db import models

class Institucion(models.Model):
    nombre = models.CharField(max_length=200)
    direccion = models.CharField(max_length=300)
    telefono = models.CharField(max_length=15)
    email = models.EmailField()
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class Servicio(models.Model):
    institucion = models.ForeignKey(Institucion, on_delete=models.CASCADE, related_name='servicios')
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class Curso(models.Model):
    institucion = models.ForeignKey(Institucion, on_delete=models.CASCADE, related_name='cursos')
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    duracion = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre
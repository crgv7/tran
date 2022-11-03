from django.db import models

# Create your models here.

class Reservacion(models.Model):
    nombre=models.CharField(max_length=15)
    apellido=models.CharField(max_length=15)
    telefono=models.CharField(max_length=7)
    fecha=models.CharField(max_length=7)
    tipo=models.CharField(max_length=7)
    vehiculo=models.CharField(max_length=7)
    costo=models.IntegerField()
     
     